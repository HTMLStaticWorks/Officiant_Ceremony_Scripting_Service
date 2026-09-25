import os
import glob
import re

files_to_update = glob.glob('*.html')

standard_menu = f'''   <!-- Mobile Menu -->
   <div class="hidden xl:hidden bg-white dark:bg-gray-900 border-b border-gray-200 dark:border-gray-800" id="mobile-menu">
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
   </div>
  </header>'''

for filepath in files_to_update:
    if filepath in ('login.html', 'signup.html'): continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    base = os.path.basename(filepath)
    def get_class(target):
        if base == target:
            return 'text-brand-primary dark:text-white bg-gray-50 dark:bg-gray-800'
        return 'hover:bg-gray-50 dark:hover:bg-gray-800'
        
    menu_html = standard_menu.format(
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
    
    # Use a robust regex that handles any whitespace formatting
    # Find anything matching id="mobile-menu" up to </header>
    new_content, count = re.subn(
        r'<div[^>]*id="mobile-menu"[^>]*>.*?</header>',
        menu_html,
        content,
        flags=re.DOTALL
    )
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
