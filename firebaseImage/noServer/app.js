// Dropzone.autoDiscover = false;

$(document).ready(function () {
  $("#myDropzone").dropzone({
    accept: function (file, done) {
        alert();
      done("Here you can write anything");
      $(".dz-preview").last().toggleClass("dz-error dz-success");
    },
  });
});
