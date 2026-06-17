// Fullpage functionality with pure JavaScript
document.addEventListener('DOMContentLoaded', function() {
    const sections = document.querySelectorAll('.section');
    const navLinks = document.querySelectorAll('.nav-link');
    let currentSection = 0;
    let isScrolling = false;

    // Initialize scroll indicator
    createScrollIndicator();

    // Smooth scroll to section
    function scrollToSection(index) {
        if (index < 0 || index >= sections.length) return;
        
        isScrolling = true;
        sections[index].scrollIntoView({ behavior: 'smooth' });
        currentSection = index;
        
        // Update active states
        updateActiveStates();
        
        setTimeout(() => {
            isScrolling = false;
        }, 1000);
    }

    // Update active states for navigation and scroll indicator
    function updateActiveStates() {
        // Update navigation
        navLinks.forEach((link, index) => {
            link.classList.remove('active');
            if (index === currentSection) {
                link.classList.add('active');
            }
        });

        // Update scroll indicator
        const dots = document.querySelectorAll('.scroll-dot');
        dots.forEach((dot, index) => {
            dot.classList.remove('active');
            if (index === currentSection) {
                dot.classList.add('active');
            }
        });

        // Update section active class
        sections.forEach((section, index) => {
            section.classList.remove('active');
            if (index === currentSection) {
                section.classList.add('active');
            }
        });
    }

    // Create scroll indicator dots
    function createScrollIndicator() {
        const indicator = document.createElement('div');
        indicator.className = 'scroll-indicator';
        
        sections.forEach((section, index) => {
            const dot = document.createElement('div');
            dot.className = 'scroll-dot';
            if (index === 0) dot.classList.add('active');
            
            dot.addEventListener('click', () => {
                scrollToSection(index);
            });
            
            indicator.appendChild(dot);
        });
        
        document.body.appendChild(indicator);
    }

    // Handle wheel scroll for fullpage effect
    let wheelTimeout;
    document.addEventListener('wheel', function(e) {
        if (isScrolling) return;
        
        clearTimeout(wheelTimeout);
        wheelTimeout = setTimeout(() => {
            if (e.deltaY > 0) {
                scrollToSection(currentSection + 1);
            } else {
                scrollToSection(currentSection - 1);
            }
        }, 50);
    }, { passive: true });

    // Handle keyboard navigation
    document.addEventListener('keydown', function(e) {
        if (e.key === 'ArrowDown' || e.key === 'PageDown') {
            e.preventDefault();
            scrollToSection(currentSection + 1);
        } else if (e.key === 'ArrowUp' || e.key === 'PageUp') {
            e.preventDefault();
            scrollToSection(currentSection - 1);
        }
    });

    // Handle navigation link clicks
    navLinks.forEach((link, index) => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetSection = Array.from(sections).find(section => 
                section.id === targetId || (index === 0 && section.id === 'home')
            );
            
            if (targetSection) {
                const targetIndex = Array.from(sections).indexOf(targetSection);
                scrollToSection(targetIndex);
            }
        });
    });

    // Handle scroll down button
    const scrollDownBtn = document.querySelector('.scroll-down');
    if (scrollDownBtn) {
        scrollDownBtn.addEventListener('click', function(e) {
            e.preventDefault();
            scrollToSection(1);
        });
    }

    // Intersection Observer for scroll-based navigation
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.5
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !isScrolling) {
                const index = Array.from(sections).indexOf(entry.target);
                if (index !== currentSection) {
                    currentSection = index;
                    updateActiveStates();
                }
            }
        });
    }, observerOptions);

    sections.forEach(section => {
        observer.observe(section);
    });

    // Animate skill bars when skills section is visible
    const skillSection = document.getElementById('skills');
    const skillBars = document.querySelectorAll('.progress-bar');
    
    const skillObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                skillBars.forEach(bar => {
                    const width = bar.style.width;
                    bar.style.width = '0%';
                    setTimeout(() => {
                        bar.style.width = width;
                    }, 100);
                });
            }
        });
    }, { threshold: 0.5 });

    if (skillSection) {
        skillObserver.observe(skillSection);
    }

    // Form submission handling
    const contactForm = document.querySelector('.contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;
            
            if (name && email && message) {
                // Show success message
                alert('메시지가 성공적으로 전송되었습니다!');
                contactForm.reset();
            } else {
                alert('모든 필드를 작성해주세요.');
            }
        });
    }

    // Navbar background change on scroll
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(255, 255, 255, 0.98)';
            navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.15)';
        } else {
            navbar.style.background = 'rgba(255, 255, 255, 0.95)';
            navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
        }
    });

    // Add parallax effect to hero section
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        const heroContent = document.querySelector('.hero-content');
        const heroImage = document.querySelector('.hero-image');
        
        if (heroContent && scrolled < window.innerHeight) {
            heroContent.style.transform = `translateY(${scrolled * 0.3}px)`;
            heroContent.style.opacity = 1 - (scrolled / window.innerHeight);
        }
        
        if (heroImage && scrolled < window.innerHeight) {
            heroImage.style.transform = `translateY(${scrolled * 0.2}px)`;
        }
    });

    // Mobile menu handling
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    
    if (navbarToggler && navbarCollapse) {
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                if (window.innerWidth < 992) {
                    navbarCollapse.classList.remove('show');
                }
            });
        });
    }

    // Initialize
    updateActiveStates();
});

// Add loading animation
window.addEventListener('load', function() {
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.5s ease';
    setTimeout(() => {
        document.body.style.opacity = '1';
    }, 100);
});
