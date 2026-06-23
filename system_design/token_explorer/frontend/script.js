const API_BASE_URL = "http://127.0.0.1:8000";

document
    .getElementById("tokenize-btn")
    .addEventListener(
        "click",
        tokenize
    );



async function tokenize() {

    const text =
        document.getElementById(
            "text-input"
        ).value;

    const mergeCount =
        Number(
            document.getElementById(
            "merge-count"
        ).value

        );

    console.log(
        "text",
        text,
        typeof text
    );


    console.log(
        "mergeCount",
        mergeCount,
        typeof mergeCount
    );
    const response =
        await fetch(
            `${API_BASE_URL}/tokenize`,
            {
                method: "POST",
                headers: {
                    "Content-Type":
                        "application/json"
                },
                body: JSON.stringify({
                    text: text,
                    num_merges: mergeCount
                })
            }
        );

    const data =
        await response.json();

    renderResults(data);
}

function renderResults(data) {

    //Word tokens
    document.getElementById(
        "word-count"
    ).textContent =
        data.word.token_count;

    document.getElementById(
        "word-output"
    ).textContent =
        data.word.tokens.join(" | ");

    //Character Tokens
    document.getElementById(
        "character-count"
    ).textContent =
        data.character.token_count;

    document.getElementById(
        "character-output"
    ).textContent =
        formatTokens(
            data.character.tokens
        ).join(" | ");

    //Character BPE Tokens
    document.getElementById(
        "character-bpe-count"
    ).textContent =
        data.character_bpe.token_count;

    document.getElementById(
        "character-bpe-output"
    ).textContent =
        formatTokens(
            data.character_bpe.tokens
        ).join(" | ");

    //Byte BPE Tokens
    document.getElementById(
        "byte-bpe-count"
    ).textContent =
        data.byte_bpe.token_count;

    // Improve byte BPE output readability

    const byteTokens =
        data.byte_bpe.tokens.map(
            token => `(${token})`
        );

    document.getElementById(
        "byte-bpe-output"
    ).textContent =
        byteTokens.join(" | ");
}


// Token format helper
function formatTokens(tokens){

    return tokens.map(token => {

        if (token === " ") {
            return "<SPACE>";
        }

        return token;
    });
}