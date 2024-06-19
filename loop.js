
    let interval; // Define interval variable globally
    let currentIndex = 0;
    // Function to loop through years
    function loopThroughYears() {
        let years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023];
        
        changeYearAndSlider(years[currentIndex]);
        

        // Initial change
        changeYear(years[currentIndex]);

        // Function to change year and update slider
        function changeYearAndSlider(year) {
            changeYear(year);
            updateSliderFromDropdown(year);
        }

        // Interval to change year every 5 seconds
        interval = setInterval(() => {
            currentIndex = (currentIndex + 1) % years.length;
            changeYearAndSlider(years[currentIndex]);
        }, 4000);

        // Function to stop the interval
        function stopLooping() {
            clearInterval(interval);
        }

        // Stop looping if user interacts with dropdown or slider
        document.getElementById('year-select').addEventListener('change', stopLooping);
        document.getElementById('yearSlider').addEventListener('input', stopLooping);
        }

        // Function to restart the loop
        function restartLoop() {
        clearInterval(interval);
        loopThroughYears();
        }

        // Call the looping function when the page loads
        window.onload = function() {
        // loopThroughYears();
        
        // Add event listener to restart button
        document.getElementById('restart-loop-btn').addEventListener('click', restartLoop);
        };
