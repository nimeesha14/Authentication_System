document.addEventListener("DOMContentLoaded", function () {
    const fileSearchInput = document.getElementById("fileSearchInput");
    const documentTableBody = document.getElementById("documentTableBody");

    if (fileSearchInput && documentTableBody) {
        fileSearchInput.addEventListener("input", function () {
            const searchValue = this.value.toLowerCase().trim();
            const rows = documentTableBody.querySelectorAll("tr");
            let visibleCount = 0;

            rows.forEach(function (row) {
                if (row.id === "noSearchResultRow") return;

                const rowText = row.textContent.toLowerCase().trim();

                if (rowText.includes(searchValue)) {
                    row.style.display = "";
                    visibleCount++;
                } else {
                    row.style.display = "none";
                }
            });

            let noResultRow = document.getElementById("noSearchResultRow");

            if (visibleCount === 0) {
                if (!noResultRow) {
                    noResultRow = document.createElement("tr");
                    noResultRow.id = "noSearchResultRow";
                    noResultRow.innerHTML = `
                        <td colspan="8" class="text-center text-muted py-4">
                            No file found.
                        </td>
                    `;
                    documentTableBody.appendChild(noResultRow);
                } else {
                    noResultRow.style.display = "";
                }
            } else {
                if (noResultRow) {
                    noResultRow.style.display = "none";
                }
            }
        });
    }
});