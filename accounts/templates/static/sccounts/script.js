const API_KEY = "TASK1_API_KEY_9F3A7C2025";
const BASE_URL = "http://127.0.0.1:8000/api";

async function register() {
  const data = {
    username: document.getElementById("username").value,
    email: document.getElementById("email").value,
    password: document.getElementById("password").value,
    phone: document.getElementById("phone").value,
  };

  const res = await fetch(`${BASE_URL}/register/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-API-KEY": API_KEY
    },
    body: JSON.stringify(data)
  });

  const result = await res.json();
  document.getElementById("msg").innerText = JSON.stringify(result);
}

async function login() {
  const data = {
    username: document.getElementById("username").value,
    password: document.getElementById("password").value,
  };

  const res = await fetch(`${BASE_URL}/login/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-API-KEY": API_KEY
    },
    body: JSON.stringify(data)
  });

  const result = await res.json();
  document.getElementById("msg").innerText = JSON.stringify(result);
}
