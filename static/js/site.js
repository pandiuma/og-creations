
document.addEventListener("DOMContentLoaded", function () {

    // Mobile navigation

    const menuButton = document.querySelector(".menu-toggle");

    const navigation = document.querySelector(".navigation");

    if (menuButton && navigation) {

        menuButton.addEventListener("click", function () {

            navigation.classList.toggle("open");

        });

        navigation.querySelectorAll("a").forEach(function (link) {

            link.addEventListener("click", function () {

                navigation.classList.remove("open");

            });

        });

    }


    // Portfolio filtering

    const filterButtons = document.querySelectorAll(
        ".filter-buttons button"
    );

    const portfolioCards = document.querySelectorAll(
        ".portfolio-card"
    );

    filterButtons.forEach(function (button) {

        button.addEventListener("click", function () {

            filterButtons.forEach(function (item) {

                item.classList.remove("active");

            });

            button.classList.add("active");

            const selectedCategory = button.dataset.filter;

            portfolioCards.forEach(function (card) {

                const cardCategory = card.dataset.category;

                if (
                    selectedCategory === "all" ||
                    selectedCategory === cardCategory
                ) {

                    card.hidden = false;

                } else {

                    card.hidden = true;

                }

            });

        });

    });

});


/* =========================================
   OUR WORKS CATEGORY FILTER
========================================= */

document.addEventListener("DOMContentLoaded", function () {

    const filterButtons = document.querySelectorAll(".work-filter");
    const projectCards = document.querySelectorAll(".work-project-card");

    filterButtons.forEach(function (button) {

        button.addEventListener("click", function () {

            const selectedCategory = button.dataset.filter;

            filterButtons.forEach(function (item) {
                item.classList.remove("active");
            });

            button.classList.add("active");

            projectCards.forEach(function (card) {

                const projectCategory = card.dataset.category;

                if (
                    selectedCategory === "all" ||
                    projectCategory === selectedCategory
                ) {
                    card.style.display = "";
                } else {
                    card.style.display = "none";
                }

            });

        });

    });

});

