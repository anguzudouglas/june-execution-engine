let editor;

let uploadedFiles = [];

require.config({
    paths: {
        vs: "https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.52.2/min/vs"
    }
});

require(
    ["vs/editor/editor.main"],
    function () {

        editor = monaco.editor.create(
            document.getElementById(
                "editor"
            ),
            {
                value:
`print("June Python Sandbox")
`,
                language: "python",
                theme: "vs-dark",
                automaticLayout: true,
                fontSize: 15,
                minimap: {
                    enabled: false
                }
            }
        );
    }
);

const output =
    document.getElementById(
        "output"
    );

const runBtn =
    document.getElementById(
        "run-btn"
    );

const uploadBtn =
    document.getElementById(
        "upload-btn"
    );

const uploadedFilesContainer =
    document.getElementById(
        "uploaded-files"
    );

const terminalContainer =
    document.getElementById(
        "terminal-container"
    );

const toggleTerminalBtn =
    document.getElementById(
        "toggle-terminal"
    );

const toggleTerminalTopBtn =
    document.getElementById(
        "toggle-terminal-top"
    );

const responseTab =
    document.getElementById(
        "response-tab"
    );

const artifactsTab =
    document.getElementById(
        "artifacts-tab"
    );

const responsePanel =
    document.getElementById(
        "response-panel"
    );

const artifactsPanel =
    document.getElementById(
        "artifacts-panel"
    );

const artifactGrid =
    document.getElementById(
        "artifact-grid"
    );

toggleTerminalBtn.addEventListener(
    "click",
    () => {

        terminalContainer.classList.toggle(
            "hidden-terminal"
        );
    }
);

toggleTerminalTopBtn.addEventListener(
    "click",
    () => {

        terminalContainer.classList.toggle(
            "hidden-terminal"
        );
    }
);

responseTab.addEventListener(
    "click",
    () => {

        responsePanel.style.display =
            "block";

        artifactsPanel.style.display =
            "none";

        responseTab.classList.add(
            "active-tab"
        );

        artifactsTab.classList.remove(
            "active-tab"
        );
    }
);

artifactsTab.addEventListener(
    "click",
    () => {

        responsePanel.style.display =
            "none";

        artifactsPanel.style.display =
            "block";

        artifactsTab.classList.add(
            "active-tab"
        );

        responseTab.classList.remove(
            "active-tab"
        );
    }
);

runBtn.addEventListener(
    "click",
    async () => {

        output.textContent =
            "Executing...";

        artifactGrid.innerHTML = "";

        try {

            const response =
                await fetch(
                    "/execute",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({
                            code:
                                editor.getValue(),

                            uploads:
                                uploadedFiles
                        })
                    }
                );

            const data =
                await response.json();

            renderResponse(data);

            renderArtifacts(
                data.artifacts || []
            );

        } catch (err) {

            output.innerHTML = `
<div class="stderr">
${escapeHtml(
    err.toString()
)}
</div>
`;
        }
    }
);

uploadBtn.addEventListener(
    "click",
    async () => {

        const input =
            document.getElementById(
                "file-input"
            );

        const files =
            input.files;

        for (const file of files) {

            const formData =
                new FormData();

            formData.append(
                "file",
                file
            );

            const response =
                await fetch(
                    "/upload",
                    {
                        method: "POST",
                        body: formData
                    }
                );

            const data =
                await response.json();

            uploadedFiles.push({
                upload_id:
                    data.upload_id,

                filename:
                    data.filename
            });

            const div =
                document.createElement(
                    "div"
                );

            div.className =
                "upload-item";

            div.innerHTML = `
<strong>
${data.filename}
</strong>

<br>

Upload ID:
${data.upload_id}
`;

            uploadedFilesContainer
                .appendChild(div);
        }
    }
);

function loadExample(type) {

    const examples = {

        raw:
`print("Hello World")

x = 10
y = 20

print(x + y)
`,

        filegen:
`with open(
    "hello.txt",
    "w"
) as f:

    f.write(
        "Hello from sandbox"
    )

print("file generated")
`,

        analysis:
`import pandas as pd

df = pd.read_csv(
    "sales.csv"
)

print(df.head())

summary = df.describe()

summary.to_csv(
    "summary.csv"
)

print(summary)
`,

        chart:
`import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,30,20,40]

plt.plot(x, y)

plt.title("Sales")

plt.savefig(
    "sales_chart.png"
)

print("chart generated")
`
    };

    editor.setValue(
        examples[type]
    );
}

function renderResponse(data) {

    let html = "";

    if (data.success) {

        html += `
<div class="stdout">

SUCCESS

</div>
`;

    } else {

        html += `
<div class="stderr">

ERROR

</div>
`;
    }

    if (data.stdout) {

        html += `
<div class="stdout">

STDOUT:

${escapeHtml(
    data.stdout
)}

</div>
`;
    }

    if (data.stderr) {

        html += `
<div class="stderr">

STDERR:

${escapeHtml(
    data.stderr
)}

</div>
`;
    }

    if (data.error) {

        html += `
<div class="stderr">

ERROR:

${escapeHtml(
    JSON.stringify(
        data.error,
        null,
        2
    )
)}

</div>
`;
    }

    output.innerHTML = html;
}

function renderArtifacts(
    artifacts
) {

    artifactGrid.innerHTML = "";

    for (const artifact of artifacts) {

        const card =
            document.createElement(
                "div"
            );

        card.className =
            "artifact-card";

        let preview = "";

        const isImage =
            artifact.filename.endsWith(
                ".png"
            ) ||

            artifact.filename.endsWith(
                ".jpg"
            ) ||

            artifact.filename.endsWith(
                ".jpeg"
            );

        if (isImage) {

            preview = `
<div class="artifact-preview">

<img
    src="${artifact.url}"
/>

</div>
`;
        }

        card.innerHTML = `
<h3>
${artifact.filename}
</h3>

<p>
${artifact.size} bytes
</p>

${preview}

<div class="artifact-actions">

<a
    href="${artifact.url}"
    target="_blank"
    class="download-btn"
>
    Open
</a>

</div>
`;

        artifactGrid.appendChild(
            card
        );
    }
}

function escapeHtml(text) {

    const div =
        document.createElement(
            "div"
        );

    div.innerText = text;

    return div.innerHTML;
}
