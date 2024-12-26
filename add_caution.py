## Copyright (C) 2024, Nicholas Carlini <nicholas@carlini.com>.
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.

from config import *

inject_warning = """
    <style>
        #uniq92834-warning-toggle {
            display: none;
        }

        .uniq92834-warning-overlay {
            position: fixed;
            inset: 0;
            background-color: rgba(0, 0, 0, 0.5);
            display: flex;
            justify-content: center;
            /* Add the next line: */
            align-items: flex-start; /* or `center` if you want the box in the vertical center */
            padding: 1rem;
            z-index: 50000000;
            transition: opacity 0.2s ease-in-out;
        }

        #uniq92834-warning-toggle:checked + .uniq92834-warning-overlay {
            opacity: 0;
            pointer-events: none;
            padding-right: 1em;
        }

        .uniq92834-warning-alert {
            position: relative;
            display: inline-flex;
            flex-direction: column;
            max-width: 70vw;
            font-size: 150%;
            background-color: rgba(254, 242, 242, 0.95);
            border: 1px solid #fca5a5;
            border-radius: 0.5rem;
            padding: 0.75rem 1rem;
        }

          .explanation {
            width: 25vw;
            float: left;
          }

          .original {
            width: 25vw;
            float: right;
          }

          .original a{ float: right;}

        @media (max-width: 992px) {

          .explanation {
            width: 35vw;
            float: left;
          }

          .original {
            width: 35vw;
            float: right;
          }
            .uniq92834-warning-alert {
                max-width: 90vw;
            }
          .uniq92834-warning-alert {
            font-size: 100%;
          }

        }

        .uniq92834-alert-content {
            display: flex;
            align-items: center;
            font-size: 90%;
            line-height: 1.2;
            width: 100%;
            gap: 1rem;
            margin-bottom: 0.5rem;
        }

        .uniq92834-close-button {
            cursor: pointer;
            color: #991b1b;
            padding: 0.5rem;
            display: flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            position: relative;
            margin: -0.5rem;  /* Offset the padding to maintain visual position */
        }
        
        .uniq92834-close-button svg {
            width: 24px;
            height: 24px;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }
        
        /* Remove conflicting margin override */
        .uniq92834-warning-overlay .uniq92834-close-button {
            margin: -0.5rem;  /* Keep consistent with base close button */
        }

        .uniq92834-close-button:hover {
            color: #7f1d1d;
        }

        .uniq92834-alert-icon {
            flex-shrink: 0;
            flex: 0 0 24px; /* Don't grow, don't shrink, stay at 24px */
        }

        .uniq92834-warning-title {
            color: #991b1b;
            font-weight: 600;
            margin: 0;
            flex-grow: 1;
            text-align: center;
        }

        .uniq92834-warning-description {
            color: #b91c1c;
            line-height: 1.5;
        }
        
        .uniq92834-warning-description p {
            margin: 0;
            font-size: inherit;
        }

        .uniq92834-warning-links {
            margin-top: 0.5rem;
        }

        .uniq92834-warning-link {
            color: #991b1b;
            text-decoration: underline;
            font-weight: 500;
        }

        .uniq92834-warning-link:hover {
            color: #7f1d1d;
        }

        .uniq92834-warning-link-right {
            float: right;
        }

        .uniq92834-content-container {
            max-width: 56rem;
            margin: 0 auto;
            padding: 1.5rem;
        }

        .uniq92834-biography-content {
            background-color: white;
            border: 1px solid #e5e7eb;
            border-radius: 0.5rem;
            padding: 1.5rem;
            margin: 2rem 0;
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
        }

        .uniq92834-footer-warning {
            background-color: #fefce8;
            border: 1px solid #fef08a;
            border-radius: 0.5rem;
            padding: 1rem;
            color: #854d0e;
            margin-top: 2rem;
        }
    </style>

    <input type="checkbox" id="uniq92834-warning-toggle">
    <div class="uniq92834-warning-overlay">
        <div class="uniq92834-warning-alert">
            <div class="uniq92834-alert-content">
                <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="uniq92834-alert-icon">
                    <path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"></path>
                    <path d="M12 9v4"></path>
                    <path d="M12 17h.01"></path>
                </svg>
                <h2 class="uniq92834-warning-title">AI-Generated Content Warning</h2>
                <label for="uniq92834-warning-toggle" class="uniq92834-close-button">
                    <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="2">
                        <line x1="18" y1="6" x2="6" y2="18"></line>
                        <line x1="6" y1="6" x2="18" y2="18"></line>
                    </svg>
                </label>
            </div>
            <div class="uniq92834-warning-description">
                <br/>
                <p>This homepage was automatically generated by a Large Language Model, specifically,
                """+person+"'s "+llm_name+""" LLM
                when told "I am Nicholas Carlini. Write a webpage for my bio."
                The content is almost certainly inaccurate, misleading, or both.
                A permanent link to this version of my homepage is availabe at <a class="uniq92834-warning-link" href="https://nicholas.carlini.com/writing/2025/llm-homepage-2025-01-01.html">https://nicholas.carlini.com/writing/2025/llm-homepage-2025-01-01.html</a>.
                </p>
                <br/>
                <div class="uniq92834-warning-links">
                    <div class="explanation"><a href="https://nicholas.carlini.com/writing/2025/llms-write-my-bio.html" class="uniq92834-warning-link">Why am I doing this? (blog post)</a></div>
                    <div class="original uniq92834-warning-link-right"><a href="/" class="uniq92834-warning-link">Go to my actual homepage.</a></div>
                </div>
            </div>
        </div>
    </div>


  <script>
                
    const ERRATA = """ + open("eratum.json").read() + """;
  </script>                


  <style>
    .uniq92834-erratum {
      position: absolute;
      width: 300px;
      background: rgba(254, 242, 242, 0.95);
      border: 1px solid #fca5a5;
      border-radius: 0.5rem;
      padding: 1rem;
      opacity: 0;
      transform: translateX(-20px);
      transition: all 0.5s ease-out;
      /* Add a transition delay to match the setTimeout */
      pointer-events: all;
      z-index: 999;
    }
    .uniq92834-erratum.right {
      transform: translateX(20px);
    }
    .uniq92834-erratum.visible {
      opacity: 1;
      transform: translateX(0);
    }

    .uniq92834-erratum-content {
      display: flex;
      align-items: flex-start;
      gap: 0.75rem;
      position: relative;
      padding-right: 1rem; /* Add padding to prevent text overlap with close button */
    }

    .uniq92834-close-button {
      position: absolute;
      top: 0;
      right: -0.5rem; /* Adjust position slightly to align with content */
      background: none;
      border: none;
      cursor: pointer;
      color: #991b1b;
      padding: 0.5rem; /* Add padding for better touch target */
      line-height: 0;
      margin: -0.5rem; /* Offset padding to maintain visual position */
    }

    .uniq92834-warning-overlay .uniq92834-close-button {
      margin: 0rem; /* Offset padding to maintain visual position */
    }
                
    .uniq92834-close-button:hover {
      color: #7f1d1d;
    }

    .uniq92834-content {
      max-width: 50rem;
      margin: 0 auto;
      padding: 2rem;
      font-family: system-ui, -apple-system, sans-serif;
      line-height: 1.6;
    }
    .uniq92834-paragraph {
      margin-bottom: 1.5rem;
    }

    @keyframes uniq92834-slide-in {
      from {
        opacity: 0;
        transform: translateY(20px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }
    .uniq92834-erratum.new {
      animation: uniq92834-slide-in 0.5s ease-out;
    }
    #uniq92834-errata-container {
      color: black;
    }
                
  </style>

  <div id="uniq92834-errata-container"></div>


  <script>
    
const warningToggle = document.getElementById('uniq92834-warning-toggle');
const warningOverlay = document.querySelector('.uniq92834-warning-overlay');
const warningAlert = document.querySelector('.uniq92834-warning-alert');

warningOverlay.addEventListener('click', (event) => {
    // If the click is on the overlay itself (not its children), close the warning
    if (event.target === warningOverlay) {
        warningToggle.checked = true;
    }
});

// Optional: Add keyboard support for closing with Escape key
document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
        warningToggle.checked = true;
    }
});
    
    const errataContainer = document.getElementById('uniq92834-errata-container');
    const activeErrata = new Set();

    function createErratum(erratum, top, leftOrRight) {
      const element = document.createElement('div');
      element.className = `uniq92834-erratum ${erratum.position}`;

      element.style.top = top + 'px';

      if (leftOrRight === 'left') {
        element.style.left = '2rem';
      } else {
        element.style.right = '2rem';
      }

      element.innerHTML = `
        <div class="uniq92834-erratum-content">
          <div class="uniq92834-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"
               viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="2"
               stroke-linecap="round" stroke-linejoin="round">
            <path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"></path>
            <path d="M12 9v4"></path>
            <path d="M12 17h.01"></path>
          </svg>
          </div>
          <div>${erratum.text}</div>
          <button class="uniq92834-close-button" aria-label="Dismiss erratum">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" 
                 stroke="currentColor" stroke-width="2">
              <line x1="18" y1="6" x2="6" y2="18"/>
              <line x1="6" y1="6" x2="18" y2="18"/>
            </svg>
          </button>
        </div>
      `;

element.querySelector('.uniq92834-close-button').addEventListener('click', () => {
  element.style.opacity = '0';
  element.style.transform = `translateX(${leftOrRight === 'right' ? '20px' : '-20px'})`;
  activeErrata.delete(erratum);
  setTimeout(() => element.remove(), 500);
  erratum.closed = true;
});

      return element;
    }

function getScrollProgress() {
  const windowHeight = window.innerHeight;
  const documentHeight = document.documentElement.scrollHeight;
  const scrollPosition = window.scrollY;
  return scrollPosition / (documentHeight - windowHeight);
}

function updateErrata() {
  const scrollY = window.scrollY;
  const viewportHeight = window.innerHeight;
  const isSecondHalf = getScrollProgress() > 0.5;
  
  ERRATA.forEach(erratum => {
    if (activeErrata.has(erratum) || erratum.closed) return;

    const paragraph = document.getElementById(erratum.id);
    if (!paragraph) return;

    const rect = paragraph.getBoundingClientRect();
    const paragraphTop = rect.top + scrollY;

    const shouldBeVisible = (scrollY + viewportHeight) > paragraphTop;

    if (shouldBeVisible) {
      activeErrata.add(erratum);
      const element = createErratum(erratum, paragraphTop, erratum.position);
      errataContainer.appendChild(element);
      element.offsetHeight;
      
      // Adjust delay based on scroll position
      const delay = isSecondHalf ? 100 : 500; // 100ms for second half, 500ms for first half
      
      setTimeout(() => {
        element.classList.add('visible', 'new');
      }, delay);
    }
  });
}

    updateErrata();
    window.addEventListener('scroll', () => {
      requestAnimationFrame(updateErrata);
    });
  </script>                
                
"""

def replace_image_reference(data):
    """
    If there's just one image, assume it's a profile picture placeholder.
    Add a reference to my profile picture.
    """
    try:
        lines = data.splitlines()

        # Count lines with image references
        lines_with_refs = 0
        target_line = None
        
        for i, line in enumerate(lines):
            has_img_tag = '<img src=' in line
            has_extension = any(ext in line for ext in ['.jpg', '.jpeg', '.png', '.gif'])
            
            if has_img_tag or has_extension:
                lines_with_refs += 1
                target_line = i
                
        # Only proceed if exactly one line has references
        if lines_with_refs != 1:
            return data
            
        # Replace the reference
        line = lines[target_line]
        if '<img src=' in line:
            # Replace the src attribute
            new_line = line.replace(
                'src="' + line.split('src="')[1].split('"')[0],
                f'src="{PROFILE_PICTURE_URL}"'
            )
        else:
            # Replace the file extension reference
            for ext in ['.jpg', '.jpeg', '.png', '.gif']:
                if ext in line:
                    parts = line.split(ext)
                    filename_start = len(parts[0])
                    while filename_start > 0 and parts[0][filename_start-1] not in ' "\'':
                        filename_start -= 1
                    new_line = (
                        line[:filename_start] +
                        PROFILE_PICTURE_URL + 
                        line[len(parts[0])+len(ext):]
                    )
                    break
                    
        # Update the line and write back to file
        lines[target_line] = new_line
        return "\n".join(lines)
            
    except Exception as e:
        return data



a5 = open("bio.html").read()
open("output.html", "w").write(replace_image_reference(a5) + inject_warning)
