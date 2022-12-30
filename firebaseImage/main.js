const firebaseConfig = {
  apiKey: "AIzaSyAzAG0a_ribj20DRAWaDNiw5B2wvtOcpYk",
  authDomain: "personid-9e533.firebaseapp.com",
  databaseURL: "https://personid-9e533-default-rtdb.firebaseio.com",
  projectId: "personid-9e533",
  storageBucket: "personid-9e533.appspot.com",
  messagingSenderId: "247603082330",
  appId: "1:247603082330:web:e71b378a57133300109463",
};

firebase.initializeApp(firebaseConfig);
let db = firebase.database();

const insert = (columnName, id, data) => {
  db.ref(columnName + "/" + id).set(data);
};

var uploadFile = async (event) => {
  // var upload = Upload({ apiKey: "public_12a1xtG8Tbmx7Ykw1c6N4ivNFpTT" });
  // var file = event.target.files[0];
  // var result = await upload.uploadFile(file);
  // var { fileUrl, filePath } = result;

  // console.log(filePath);

  const htmlProcess = () => {
    $(".spinner-border").addClass("d-none");
    $("#uploadBtn").show(750);
  };

  const formData = new FormData();
  formData.append("file", event.target.files[0]);
  formData.append("upload_preset", "docs_upload_example_us_preset");

  $.ajax({
    url: "https://api.cloudinary.com/v1_1/demo/image/upload",
    data: formData,
    cache: false,
    contentType: false,
    processData: false,
    method: "POST",
    type: "POST",
    success: function (data) {
      insert("imageResim", new Date().getTime(), { file: data.url });

      Swal.fire("Resminiz Başarılı Bir Şekilde Yüklendi !", "", "success");
      htmlProcess();
    },
    error: () => {
      Swal.fire("Lütfen Dosya Uzantınıza Dikkat Ediniz !", "", "warning");
      htmlProcess();
    },
  });
};

window.URL = window.URL || window.webkitURL;
function displayImages(event) {
  let files = event.target.files;
  let info = document.getElementById("info");
  info.innerHTML = "";
  for (let i = 0; i < files.length; i++) {
    $("#uploadBtn").show(750);
    let src = URL.createObjectURL(files[i]);
    info.innerHTML += `<img src="${src}" class="rounded d-block m-auto"
            style="height: 300px;   max-width: 300px;"> `;
  }
}

$("#uploadBtn").hide();
$("#photoChange").click(function (e) {
  document.getElementById("photoBtn").click();
  $("#uploadBtn").hide();
});
$("#photoBtn").change(function (event) {
  displayImages(event);
  $("#uploadBtn").click(function (e) {
    $("#uploadBtn").hide();
    $(".spinner-border").removeClass("d-none");
    uploadFile(event);
  });
});
