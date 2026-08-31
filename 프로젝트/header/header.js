/* ==========================================================
   집찾Go Header
   File : header.js
========================================================== */

document.addEventListener("DOMContentLoaded", () => {

    const header = document.querySelector(".header");
    const progressBar = document.querySelector(".progress-bar-scroll");
    const btnTop = document.querySelector("#btnTop");
    const navLinks = document.querySelectorAll(".nav-link");
    const navbarCollapse = document.querySelector(".navbar-collapse");

    /* ======================================================
       Sticky Header
    ====================================================== */

    function stickyHeader() {

        if (window.scrollY > 80) {

            header.classList.add("scrolled");

        } else {

            header.classList.remove("scrolled");

        }

    }

    stickyHeader();

    window.addEventListener("scroll", stickyHeader);

    /* ======================================================
       Scroll Progress
    ====================================================== */

    function scrollProgress() {

        const scrollTop = window.scrollY;

        const docHeight =
            document.documentElement.scrollHeight - window.innerHeight;

        const progress = (scrollTop / docHeight) * 100;

        progressBar.style.width = progress + "%";

    }

    scrollProgress();

    window.addEventListener("scroll", scrollProgress);

    /* ======================================================
       Back To Top
    ====================================================== */

    btnTop.addEventListener("click", function (e) {

        e.preventDefault();

        window.scrollTo({

            top: 0,

            behavior: "smooth"

        });

    });

    /* ======================================================
       Active Menu
    ====================================================== */

    navLinks.forEach(link => {

        link.addEventListener("click", function () {

            navLinks.forEach(item => {

                item.classList.remove("active");

            });

            this.classList.add("active");

        });

    });

    /* ======================================================
       Hero Fade Animation
    ====================================================== */

    const observer = new IntersectionObserver(

        entries => {

            entries.forEach(entry => {

                if (entry.isIntersecting) {

                    entry.target.classList.add("fade-up");

                }

            });

        },

        {

            threshold: .2

        }

    );

    document.querySelectorAll(".fade-up,.zoom-in").forEach(el => {

        observer.observe(el);

    });

    /* ======================================================
       Mobile Menu Close
    ====================================================== */

    navLinks.forEach(link => {

        link.addEventListener("click", () => {

            if (window.innerWidth < 992) {

                bootstrap.Collapse.getOrCreateInstance(navbarCollapse).hide();

            }

        });

    });

    /* ======================================================
       Floating Button Show
    ====================================================== */

    const floatingNav = document.querySelector(".floating-nav");

    function floatingVisible() {

        if (window.scrollY > 300) {

            floatingNav.style.opacity = "1";

            floatingNav.style.pointerEvents = "auto";

        } else {

            floatingNav.style.opacity = "0";

            floatingNav.style.pointerEvents = "none";

        }

    }

    floatingVisible();

    window.addEventListener("scroll", floatingVisible);

    /* ======================================================
       Smooth Scroll
    ====================================================== */

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {

        anchor.addEventListener("click", function (e) {

            const target = document.querySelector(this.getAttribute("href"));

            if (!target) return;

            e.preventDefault();

            target.scrollIntoView({

                behavior: "smooth"

            });

        });

    });

});