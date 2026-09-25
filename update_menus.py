import os
import re

files_to_update = [
    'about.html',
    'services.html',
    'ceremony-styles.html',
    'sample-scripts.html',
    'booking.html',
    'contact.html',
    '404.html',
    'coming-soon.html'
]

standard_actions = '''      <div class="flex xl:hidden items-center gap-4">
       <button aria-label="Toggle RTL" class="rtl-toggle w-10 h-10 rounded-full flex items-center justify-center border border-gray-200 dark:border-gray-700 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors">
        <i class="w-5 h-5" data-lucide="arrow-left-right">
        </i>
       </button>
       <button aria-label="Toggle Dark Mode" class="theme-toggle w-10 h-10 rounded-full flex items-center justify-center border border-gray-200 dark:border-gray-700 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors">
        <i class="w-5 h-5" data-lucide="moon">
        </i>
       </button>
       <button aria-expanded="false" class="w-10 h-10 rounded-full flex items-center justify-center border border-gray-200 dark:border-gray-700 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white focus:outline-none" id="mobile-menu-btn">
        <i class="w-6 h-6" data-lucide="menu">
        </i>
       </button>
      </div>'''

for filepath in files_to_update:
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the actions div
    content = re.sub(
        r'<div class="flex xl:hidden items-center gap-4">.*?</div>\s*</div>\s*</div>',
        standard_actions + '\\n     </div>\\n    </div>',
        content,
        flags=re.DOTALL
    )
    
    # Active class logic
    base = os.path.basename(filepath)
    def get_class(target):
        if base == target:
            return 'text-brand-primary dark:text-white bg-gray-50 dark:bg-gray-800'
        return 'hover:bg-gray-50 dark:hover:bg-gray-800'
    
    standard_menu = f'''   <div class="hidden xl:hidden bg-white dark:bg-gray-900 border-b border-gray-200 dark:border-gray-800" id="mobile-menu">
    <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3">
     <a class="block px-3 py-2 rounded-md text-base font-medium {{}}" href="index.html">
      Home 1
     </a>
     <a class="block px-3 py-2 rounded-md text-base font-medium {{}}" href="home-2.html">
      Home 2
     </a>
     <a class="block px-3 py-2 rounded-md text-base font-medium {{}}" href="about.html">
      About
     </a>
     <a class="block px-3 py-2 rounded-md text-base font-medium {{}}" href="services.html">
      Services
     </a>
     <a class="block px-3 py-2 rounded-md text-base font-medium {{}}" href="ceremony-styles.html">
      Styles
     </a>
     <a class="block px-3 py-2 rounded-md text-base font-medium {{}}" href="sample-scripts.html">
      Scripts
     </a>
     <a class="block px-3 py-2 rounded-md text-base font-medium {{}}" href="booking.html">
      Booking
     </a>
     <a class="block px-3 py-2 rounded-md text-base font-medium {{}}" href="contact.html">
      Contact
     </a>
     <a class="block px-3 py-2 rounded-md text-base font-medium {{}}" href="dashboard.html">
      Dashboard
     </a>
     <a class="block px-3 py-2 mt-4 text-center btn-primary w-full" href="signup.html">
      Signup
     </a>
    </div>
   </div>'''
    
    standard_menu = standard_menu.format(
        get_class('index.html'),
        get_class('home-2.html'),
        get_class('about.html'),
        get_class('services.html'),
        get_class('ceremony-styles.html'),
        get_class('sample-scripts.html'),
        get_class('booking.html'),
        get_class('contact.html'),
        get_class('dashboard.html')
    )
    
    # Replace the mobile menu panel
    content = re.sub(
        r'<div class="hidden xl:hidden bg-white dark:bg-gray-900 border-b border-gray-200 dark:border-gray-800" id="mobile-menu">.*?</header>',
        standard_menu + '\\n  </header>',
        content,
        flags=re.DOTALL
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {filepath}")
