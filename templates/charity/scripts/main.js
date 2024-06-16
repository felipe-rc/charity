const form = document.querySelector("#loginInfo");

async function login () {
  async function sendData() {
  const formData = new FormData(form);
    try {
      const username = formData.get('username')
      if (username.includes('admin')) {
          console.log("ADMIN")
          window.location.href = '../pages/admin/index.html'
      } else if (username.includes('donor')) {
          window.location.href = '../pages/donor/index.html'
      } else {
          window.location.href = '../pages/aux/index.html'
      }
    } catch (e) {
      console.error(e);
    }
  }
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    sendData();
  });
}
