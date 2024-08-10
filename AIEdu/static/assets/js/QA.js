document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("btnGen").onclick = () => {
    getAnswerApi();
  };
  document.getElementById("btnSumLink").onclick = () => {
    getGenTracNghiemApi();
  };
  document.getElementById("btnSumVietAi").onclick = () => {
    getAnswerApi2();
  };
  document.getElementById("btnSpeek2").onclick = () => {
    speek2();
  };
});
const componetLoadingButton = `<img src="/static/assets/img/gif/Spin_white_bg-blue.gif" style="width: 25px ;height:25px"/>`;
async function getAnswerApi() {
  var strPragraph = document.getElementById("paragraph").value;
  if (!strPragraph) {
    window.confirm("Bạn phải nhập nội dung văn bản cần tóm tắt.");
    return;
  }
  document.querySelector("#btnGen").innerHTML = componetLoadingButton;
  document.getElementById("answer").innerHTML = "";
  document.querySelector("#btnGen").click = () => {};
  var content = [
    '"' + strPragraph + '"',
    "\n",
    `hãy tóm tắt lại  nội dung của đoạn văn bản trên bằng tiếng việt. `,
  ].join(" ");
  fetch(urlGenAiApi, {
    method: "post",
    headers: {
      "content-type": "application/json",
    },
    body: JSON.stringify({
      question: content,
    }),
  })
    .then((res) => res.json())
    .then((data) => {
      document.querySelector("#btnGen").innerHTML = "Tóm tắt";

      document.getElementById("answer").innerHTML = data.response[1][0][1];
    });
}
async function getAnswerApi2() {
  var strPragraph = document.getElementById("paragraph").value;
  if (!strPragraph) {
    window.confirm("Bạn phải nhập nội dung văn bản cần tóm tắt.");
    return;
  }
  document.querySelector("#btnSumVietAi").innerHTML = "Đang xử lý ...";
  document.getElementById("answer").innerHTML = "";
  document.querySelector("#btnSumVietAi").click = () => {};
  var content = [
    '"' + strPragraph + '"',
    "\n",
    `hãy tóm tắt lại  nội dung của đoạn văn bản trên bằng tiếng việt. `,
  ].join(" ");
  fetch(urlSummarazationVietAi, {
    method: "post",
    headers: {
      "content-type": "application/json",
    },
    body: JSON.stringify({
      paragraph: content,
    }),
  })
    .then((res) => res.json())
    .then((data) => {
      document.querySelector("#btnSumVietAi").innerHTML = "Tóm tắt";

      document.getElementById("answer").innerHTML = data.response;
    });
}
async function getGenTracNghiemApi() {
  var strLink = document.getElementById("linkWebsite").value;
  var iframe = document.getElementById('webFrame');
  // var iframeUrl = iframe.contentWindow.location.href;
  // document.getElementById("linkWebsite").value=iframeUrl
  // strLink= iframeUrl

  document.querySelector("#btnSumLink").innerHTML = componetLoadingButton;
  document.getElementById("webNoidung").innerHTML = "";
  document.querySelector("#btnSumLink").click = () => {};

  var content = [
    '"' + strLink + '"',
    "\n",
    `hãy viết lại cho tôi nội dung trang web, bằng tiếng việt. Lưu ý bỏ chích dẫn nguồn và chỉ trả lại nội dung trang web . `,
  ].join(" ");

  fetch(urlGenAiApi, {
    method: "post",
    headers: {
      "content-type": "application/json",
    },
    body: JSON.stringify({
      question: content,
    }),
  })
    .then((res) => res.json())
    .then((data) => {
      document.querySelector("#btnSumLink").innerHTML = "Submit";

      document.getElementById("webNoidung").innerHTML = data.response[1][0][1];
    });
}
function speek1() {
  document.querySelector("#btnSpeek2").innerHTML = "Đang xử lý";

  document.querySelector("#btnSpeek2").click = () => {};
  fetch(urlTextToSpeech, {
    method: "post",
    headers: {
      "content-type": "application/json",
    },
    body: JSON.stringify({
      text: document.getElementById("webNoidung").value,
    }),
  })
    .then((res) => res.json())
    .then((data) => {
      document.querySelector("#btnSpeek2").innerHTML = "Nói";
    });
}
async function speek2() {
  document.querySelector("#btnSpeek2").innerHTML = "Đang xử lý";

  document.querySelector("#btnSpeek2").click = () => {};
  data = document.getElementById("webNoidung").value;
  const response = await fetch(
    "https://api-inference.huggingface.co/models/facebook/mms-tts-vie",
    {
      headers: {
        Authorization: "Bearer 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",
      },
      method: "POST",
      body: JSON.stringify({ inputs: data }),
    }
  );
  const result = await response.blob();
  playAudioFromBlob(result);
  document.querySelector("#btnSpeek2").innerHTML = "Nói";
  return result;
}
function playAudioFromBlob(blobData) {
    const audio = new Audio();
    audio.src = URL.createObjectURL(blobData); // Tạo URL từ Blob
    audio.play(); // Phát âm thanh
}
// speek2({"inputs": "The answer to the universe is 42"}).then((response) => {
//     // Returns a byte object of the Audio wavform. Use it directly!
//     document.querySelector("#btnSpeek2").innerHTML="Nói";
// });
