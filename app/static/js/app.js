let editor;

let uploadedFiles = [];

require.config({
    paths: {
        vs: "https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.52.2/min/vs"
    }
});

require(["vs/editor/editor.main"], function () {

    editor = monaco.editor.create(
        document.getElementById("editor"),
        {
            value:
`print("June Python Sandbox")`,
            language: "python",
            theme: "vs-dark",
            automaticLayout: true,
            fontSize: 15,
            minimap: {
                enabled: false
            }
        }
    );
});

const output = document.getElementById(
    "output"
);

const runBtn = document.getElementById(
    "run-btn"
);

const uploadBtn = document.getElementById(
    "upload-btn"
);

const uploadedFilesContainer =
    document.getElementById(
        "uploaded-files"
    );

runBtn.addEventListener(
    "click",
    async () => {

        output.textContent =
            "Executing...";

        try {

            const response = await fetch(
                "/execute",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        code: editor.getValue(),
                        uploads: uploadedFiles
                    })
                }
            );

            const data = await response.json();

            output.textContent =
                JSON.stringify(
                    data,
                    null,
                    2
                );

        } catch (err) {

            output.textContent =
                err.toString();
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

        const files = input.files;

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
                <strong>${data.filename}</strong>
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
