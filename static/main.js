/**
 * Kalenderia.my.id — HTMX Active-State Manager & Mobile Drawer Controller
 */

document.addEventListener('DOMContentLoaded', () => {
    updateSidebarActiveState();
    setupHTMXAnimations();
    setupMobileDrawer();
});

// Dengarkan event swap & history restore HTMX agar status aktif sidebar 100% konsisten
document.body.addEventListener('htmx:afterSwap', () => {
    updateSidebarActiveState();
    closeMobileDrawer(); // Tutup drawer otomatis setelah navigasi HTMX di seluler
});

document.body.addEventListener('htmx:historyRestore', () => {
    updateSidebarActiveState();
    closeMobileDrawer();
});

/**
 * Memperbarui status kelas aktif pada navigasi sidebar secara presisi berbasis window.location.pathname
 */
function updateSidebarActiveState() {
    const currentPath = window.location.pathname;
    const navItems = document.querySelectorAll('#sidebar-nav .nav-item');

    if (!navItems || navItems.length === 0) return;

    navItems.forEach(item => {
        const href = item.getAttribute('data-nav-href') || item.getAttribute('href');
        const icon = item.querySelector('.nav-icon');

        let isActive = false;
        if (href === '/') {
            isActive = (currentPath === '/' || currentPath === '');
        } else if (href) {
            isActive = currentPath.startsWith(href);
        }

        if (isActive) {
            item.className = 'nav-item flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-xs font-bold bg-emerald-600 text-white shadow-md shadow-emerald-600/20 transition active-press';
            if (icon) {
                icon.classList.remove('text-slate-400');
                icon.classList.add('text-white');
            }
        } else {
            item.className = 'nav-item flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-xs font-semibold text-slate-600 hover:bg-slate-100 hover:text-slate-900 transition active-press';
            if (icon) {
                icon.classList.remove('text-white');
                icon.classList.add('text-slate-400');
            }
        }
    });
}

/**
 * Pengendali Mobile Off-Canvas Drawer (Slide-in Sidebar di Seluler)
 */
function setupMobileDrawer() {
    const toggleBtn = document.getElementById('mobile-drawer-toggle');
    const closeBtn = document.getElementById('mobile-drawer-close');
    const backdrop = document.getElementById('drawer-backdrop');

    if (toggleBtn) {
        toggleBtn.addEventListener('click', openMobileDrawer);
    }
    if (closeBtn) {
        closeBtn.addEventListener('click', closeMobileDrawer);
    }
    if (backdrop) {
        backdrop.addEventListener('click', closeMobileDrawer);
    }
}

function openMobileDrawer() {
    const sidebar = document.getElementById('sidebar-container');
    const backdrop = document.getElementById('drawer-backdrop');

    if (sidebar && backdrop) {
        sidebar.classList.remove('-translate-x-full');
        backdrop.classList.remove('hidden');
        setTimeout(() => backdrop.classList.remove('opacity-0'), 10);
        document.body.classList.add('overflow-hidden'); // Cegah background scrolling di HP
    }
}

function closeMobileDrawer() {
    const sidebar = document.getElementById('sidebar-container');
    const backdrop = document.getElementById('drawer-backdrop');

    if (sidebar && backdrop) {
        sidebar.classList.add('-translate-x-full');
        backdrop.classList.add('opacity-0');
        setTimeout(() => backdrop.classList.add('hidden'), 300);
        document.body.classList.remove('overflow-hidden');
    }
}

/**
 * Menyiapkan penanganan animasi HTMX fade-in swap
 */
function setupHTMXAnimations() {
    document.body.addEventListener('htmx:beforeSwap', (e) => {
        const target = e.detail.target;
        if (target && target.id === 'main-content') {
            target.classList.remove('animate-fade-in');
        }
    });

    document.body.addEventListener('htmx:afterSwap', (e) => {
        const target = e.detail.target;
        if (target && target.id === 'main-content') {
            void target.offsetWidth;
            target.classList.add('animate-fade-in');
        }
    });
}
