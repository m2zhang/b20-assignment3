$(document).ready(function() {
    $("#openGradeFormButton").click(function() {
        $("#gradeForm").toggle();
    });
    $("#closeGradeFormButton").click(function() {
        $("#gradeForm").hide();
    });
});

$(document).ready(function() {
    $("#filterButton").click(function() {
        $(".student_grades tbody tr").each(function() {
            var remarkRequest = $(this).find("td:nth-child(5)").text().trim();
            if (remarkRequest === '') {
                $(this).toggle(); // Toggle visibility
            }
        });
    });
});

$(document).ready(function() {
    $("#openRemarkFormButton").click(function() {
        $("#remarkForm").show();
    });

    $("#closeRemarkFormButton").click(function() {
        $("#remarkForm").hide();
    });
});
