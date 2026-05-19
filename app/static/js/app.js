const runBtn = document.getElementById("run-btn");

const editor = document.getElementById(
    "code-editor"
);

const output = document.getElementById(
    "output"
);


runBtn.addEventListener(
    "click",
    async () => {

        output.textContent = "Running...";

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
                        code: editor.value
                    })
                }
            );

            const data = await response.json();

            output.textContent = JSON.stringify(
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
