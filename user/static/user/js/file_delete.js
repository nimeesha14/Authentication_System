document.addEventListener("DOMContentLoaded", function () {
    const selectAllCheckbox = document.getElementById("selectAllCheckbox");
    const deleteSelectedBtn = document.getElementById("deleteSelectedBtn");
    const confirmDeleteBtn = document.getElementById("confirmDeleteBtn");
    const deleteForm = deleteSelectedBtn ? deleteSelectedBtn.closest("form") : null;

    function getRowCheckboxes() {
        return document.querySelectorAll(".rowCheckbox");
    }

    function toggleDeleteButton() {
        const rowCheckboxes = getRowCheckboxes();
        let anyChecked = false;

        rowCheckboxes.forEach(function (checkbox) {
            if (checkbox.checked) {
                anyChecked = true;
            }
        });

        if (deleteSelectedBtn) {
            if (anyChecked) {
                deleteSelectedBtn.classList.remove("d-none");
            } else {
                deleteSelectedBtn.classList.add("d-none");
            }
        }
    }

    if (selectAllCheckbox) {
        selectAllCheckbox.addEventListener("change", function () {
            const rowCheckboxes = getRowCheckboxes();

            rowCheckboxes.forEach(function (checkbox) {
                checkbox.checked = selectAllCheckbox.checked;
            });

            toggleDeleteButton();
        });
    }

    document.addEventListener("change", function (e) {
        if (e.target.classList.contains("rowCheckbox")) {
            const rowCheckboxes = getRowCheckboxes();
            let allChecked = rowCheckboxes.length > 0;

            rowCheckboxes.forEach(function (checkbox) {
                if (!checkbox.checked) {
                    allChecked = false;
                }
            });

            if (selectAllCheckbox) {
                selectAllCheckbox.checked = allChecked;
            }

            toggleDeleteButton();
        }
    });

    if (deleteSelectedBtn) {
        deleteSelectedBtn.addEventListener("click", function () {
            const rowCheckboxes = getRowCheckboxes();
            let selectedCount = 0;

            rowCheckboxes.forEach(function (checkbox) {
                if (checkbox.checked) {
                    selectedCount++;
                }
            });

            if (selectedCount === 0) {
                return;
            }

            const deleteModalElement = document.getElementById("deleteConfirmModal");
            const deleteModal = new bootstrap.Modal(deleteModalElement);
            deleteModal.show();
        });
    }

    if (confirmDeleteBtn && deleteForm) {
        confirmDeleteBtn.addEventListener("click", function () {
            deleteForm.submit();
        });
    }
});