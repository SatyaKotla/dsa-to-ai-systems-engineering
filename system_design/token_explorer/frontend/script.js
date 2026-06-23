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

    const wordTokens =
        data.word.tokens
            .map(
                token =>
                    `<span class="token-chip">${token}</span>`

            ).join("");

    document.getElementById(
        "word-output"
    ).innerHTML =
        wordTokens;

    //Character Tokens
    document.getElementById(
        "character-count"
    ).textContent =
        data.character.token_count;

    const characterTokens =
        formatTokens(data.character.tokens)
            .map(
                token =>
                    `<span class="token-chip">${token}</span>`

            ).join("");

    document.getElementById(
        "character-output"
    ).innerHTML =
        characterTokens;

    //Character BPE Tokens
    document.getElementById(
        "character-bpe-count"
    ).textContent =
        data.character_bpe.token_count;

    const characterBPETokens =
        formatTokens(data.character_bpe.tokens)
            .map(
                token =>
                    `<span class="token-chip">${token}</span>`

            ).join("");

    document.getElementById(
        "character-bpe-output"
    ).innerHTML =
        characterBPETokens;

    //Byte BPE Tokens
    document.getElementById(
        "byte-bpe-count"
    ).textContent =
        data.byte_bpe.token_count;

    // Improve byte BPE output readability

    const byteTokens =
        data.byte_bpe.tokens
            .map(
                token =>
                    `<span class="token-chip">(${token})</span>`
            ).join("");

    document.getElementById(
        "byte-bpe-output"
    ).innerHTML =
        byteTokens;
}


// Token format helper
function formatTokens(tokens){

    return tokens.map(token => {

        if (token === " ") {
            return "&lt;SPACE&gt;";
        }

        return token;
    });
}