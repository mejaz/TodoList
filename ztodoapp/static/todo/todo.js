$(document).on("click", ".edit-task", function (e) {
    e.preventDefault();
    var _this = $(this);
    var task = _this.data('task');
    var id = _this.data('id');
    $("#edit-modal").val(task);
    $("#editForm").attr('action', "/todolist/editTask/" + id + '/')
    $('#exampleModalCenter').modal('show');
});