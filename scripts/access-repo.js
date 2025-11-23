// access-repo.js
const repo = "1rec3/holobionte-1rec3";
const url = `https://api.github.com/repos/${repo}`;

fetch(url)
  .then(response => {
    if (!response.ok) throw new Error("Repositorio no encontrado");
    return response.json();
  })
  .then(data => {
    console.log("Repositorio encontrado:", data.html_url);
    window.open(data.html_url, "_blank");
    console.log("🚀 Acceso exitoso al repositorio de GitHub");
  })
  .catch(error => {
    console.error("❌ Error al acceder al repositorio:", error);
  });

