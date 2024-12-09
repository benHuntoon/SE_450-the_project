# SE_450-the_project
Base avl.py file with updated code, test_avl.py file with unit tests and the avl.tstl file 

To mutate the base file simply have tstl installed as instructed here: https://howtotestit.wordpress.com/2024/02/22/a-brief-primer-on-using-tstl-and-deepstate-in-docker/

Be sure to run "tstl avl.tstl" before mutating, then "tstl_rt" to ensure a sut.py file is generated.

Once this is done run "mutate avl.py"

To get the mutation score run this command after the mutants have been generated: 'analyze_mutants avl.py "tstl_rt --timeout 10" --timeout 15 --verbose'

====
To obtain a coverage score, ensure the avl.py file is installed with the test_avl.py file in the same directory.

Then run this command to generate a coverage score: "pytest test_avl.py --cov=avl"

This will then generate the generalizd coverage score for avl.py
