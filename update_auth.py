import os
import re

for filepath, max_w in [('signup.html', 'max-w-xl'), ('login.html', 'max-w-md')]:
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already wrapped
    if 'data-aos="zoom-in">\n    <!-- Theme / Nav controls -->' in content:
        continue
        
    old_nav = '''   <!-- Theme / Nav controls -->
   <div class="fixed top-4 right-4 sm:top-6 sm:right-6 z-50 flex items-center gap-4 bg-theme-bg/50 dark:bg-gray-900/50 backdrop-blur-sm p-2 rounded-full shadow-sm sm:bg-transparent sm:backdrop-blur-none sm:shadow-none sm:p-0 sm:rounded-none">
    <button aria-label="Toggle Dark Mode" class="theme-toggle p-2 text-gray-500 hover:text-brand-primary dark:text-gray-400 dark:hover:text-white transition-colors">
     <i class="w-5 h-5" data-lucide="moon">
     </i>
    </button>
    <button class="rtl-toggle text-sm font-medium p-2 text-gray-500 hover:text-brand-primary dark:text-gray-400 dark:hover:text-white transition-colors">
     <i class="w-5 h-5" data-lucide="arrow-left-right">
     </i>
    </button>
   </div>
   <div class="''' + max_w + ''' w-full relative z-10 bg-white dark:bg-gray-800 p-8 sm:p-10 rounded-2xl shadow-2xl border border-gray-100 dark:border-gray-700" data-aos="zoom-in">'''
    
    # Use regex to replace to handle \r\n vs \n
    pattern = re.compile(re.escape(old_nav).replace(r'\n', r'\s*'), re.DOTALL)
    
    new_nav = f'''   <div class="{max_w} w-full relative z-10" data-aos="zoom-in">
    <!-- Theme / Nav controls -->
    <div class="flex justify-end mb-4 sm:mb-6">
     <div class="flex items-center gap-4 bg-theme-bg/50 dark:bg-gray-900/50 backdrop-blur-sm p-2 rounded-full shadow-sm sm:bg-transparent sm:backdrop-blur-none sm:shadow-none sm:p-0 sm:rounded-none">
      <button aria-label="Toggle Dark Mode" class="theme-toggle p-2 text-gray-500 hover:text-brand-primary dark:text-gray-400 dark:hover:text-white transition-colors">
       <i class="w-5 h-5" data-lucide="moon">
       </i>
      </button>
      <button class="rtl-toggle text-sm font-medium p-2 text-gray-500 hover:text-brand-primary dark:text-gray-400 dark:hover:text-white transition-colors">
       <i class="w-5 h-5" data-lucide="arrow-left-right">
       </i>
      </button>
     </div>
    </div>
    <div class="bg-white dark:bg-gray-800 p-8 sm:p-10 rounded-2xl shadow-2xl border border-gray-100 dark:border-gray-700">'''
    
    content = pattern.sub(new_nav, content)
    
    # Close the wrapper div right before <script> lucide.createIcons
    content = re.sub(
        r'(   </div>\s*<script>\s*lucide\.createIcons\(\);\s*</script>)',
        r'   </div>\n  </div>\n  <script>\n   lucide.createIcons();\n  </script>',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated {filepath}")
