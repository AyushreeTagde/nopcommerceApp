pytest -s -v -m "Sanity" --html=./Reports\report.html testCases/ --browser chrome
rem pytest -s -v -m "Sanity or regression" --html=./Reports\report.html testCases/ --browser chrome
rem pytest -s -v -m "Sanity and regression" --html=./Reports\report.html testCases/ --browser chrome
rem pytest -s -v -m "regression" --html=./Reports\report.html testCases/ --browser chrome


