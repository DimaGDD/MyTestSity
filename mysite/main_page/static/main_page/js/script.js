function toggleMenu() {
    const menu = document.getElementById('profileMenu');
    menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
}

function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    const mainContent = document.getElementById("main-content");

    sidebar.classList.toggle("expanded");
    mainContent.classList.toggle("shifted");
}

window.onclick = function(event) {
    if (!event.target.matches('.profile-icon')) {
        const menu = document.getElementById('profileMenu');
        if (menu.style.display === 'block') {
            menu.style.display = 'none';
        }
    }
}
