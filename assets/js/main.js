// Configuration and state management
const state = {
    theme: localStorage.getItem('theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'),
    rtl: localStorage.getItem('rtl') === 'true'
};

// Initialize App
document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initRTL();
    initMobileMenu();
    initHeaderScroll();
    initActiveNav();
    
    // Initialize AOS Animation Library
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            easing: 'ease-out-cubic',
            once: true,
            offset: 50,
            disable: window.innerWidth < 768 // Disable on small screens for performance if needed, but keeping enabled is fine for premium feel. We'll leave it on but reduce intensity in CSS if needed. Let's keep it on.
        });
    }
});

// Theme Management
function initTheme() {
    const html = document.documentElement;
    const themeToggles = document.querySelectorAll('.theme-toggle');
    
    function applyTheme(theme) {
        if (theme === 'dark') {
            html.classList.add('dark');
        } else {
            html.classList.remove('dark');
        }
        localStorage.setItem('theme', theme);
        state.theme = theme;
        
        // Update icons
        themeToggles.forEach(toggle => {
            const icon = toggle.querySelector('i');
            if (icon) {
                icon.setAttribute('data-lucide', theme === 'dark' ? 'sun' : 'moon');
                if (typeof lucide !== 'undefined') lucide.createIcons();
            }
        });
    }

    applyTheme(state.theme);

    themeToggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            applyTheme(state.theme === 'light' ? 'dark' : 'light');
        });
    });
}

// RTL Management
function initRTL() {
    const html = document.documentElement;
    const rtlToggles = document.querySelectorAll('.rtl-toggle');
    
    function applyRTL(isRTL) {
        html.setAttribute('dir', isRTL ? 'rtl' : 'ltr');
        localStorage.setItem('rtl', isRTL);
        state.rtl = isRTL;
        
        // Adjust AOS for RTL if necessary, usually it handles it gracefully.
        
        rtlToggles.forEach(toggle => {
            const text = toggle.querySelector('.rtl-text');
            if(text) text.textContent = isRTL ? 'LTR' : 'RTL';
        });
    }

    applyRTL(state.rtl);

    rtlToggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            applyRTL(!state.rtl);
        });
    });
}

// Mobile Menu
function initMobileMenu() {
    const btn = document.getElementById('mobile-menu-btn');
    const menu = document.getElementById('mobile-menu');
    
    if (btn && menu) {
        btn.addEventListener('click', () => {
            const isExpanded = btn.getAttribute('aria-expanded') === 'true';
            btn.setAttribute('aria-expanded', !isExpanded);
            menu.classList.toggle('hidden');
        });
    }
}

// Sticky Header
function initHeaderScroll() {
    const header = document.getElementById('main-header');
    if (!header) return;

    window.addEventListener('scroll', () => {
        if (window.scrollY > 20) {
            header.classList.add('glass-effect', 'shadow-sm');
            header.classList.remove('bg-transparent');
        } else {
            header.classList.remove('glass-effect', 'shadow-sm');
            header.classList.add('bg-transparent');
        }
    });
}

// Active Navigation State
function initActiveNav() {
    const currentPath = window.location.pathname;
    let currentPage = currentPath.split('/').pop();
    if (currentPage === '') currentPage = 'index.html';
    // Handle root path variations
    if (currentPage === 'Officiant%20&%20Ceremony%20Scripting%20Service' || !currentPage.endsWith('.html')) {
        currentPage = 'index.html';
    }

    const links = document.querySelectorAll('header a');
    
    links.forEach(link => {
        const href = link.getAttribute('href');
        if (!href || href === '#') return;
        
        const linkPage = href.split('/').pop();
        
        if (linkPage === currentPage && linkPage !== '') {
            if (link.classList.contains('nav-link')) {
                // Desktop Nav Link Active State
                link.classList.add('text-brand-primary', 'dark:text-white', 'after:scale-x-100', 'after:origin-bottom-left');
                link.classList.remove('text-gray-600', 'dark:text-gray-300');
            } else if (link.classList.contains('block') && link.classList.contains('px-3') && link.closest('#mobile-menu')) {
                // Mobile Menu Link Active State
                link.classList.add('text-brand-primary', 'dark:text-brand-light', 'bg-brand-primary/10', 'dark:bg-gray-800');
                link.classList.remove('text-gray-500', 'text-gray-900', 'dark:text-gray-400', 'dark:text-white');
            }
        }
    });
}
