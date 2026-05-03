CPG companies face many complex operational challenges and have access to limited
resources to solve them. One example of these issues are shortages - when a brand does not
have enough product to fulfill all of the committed orders. Even more challenging, different
distributors and retailers will charge different penalty rates for shortages (and may even change
the penalty by month). In this instance, brands do not have a programmatic way of determining
how much of a purchase order (POs) to fulfill.

For example, say we have a 90% fill rate requirement for Target with a 1% penalty rate. If the
PO is for 100 units and a total amount of $150 but we only deliver 80 units, then we will be fined
$0.15 = (10 units * 0.01 * $1.50/unit).

Please complete the following illustration of that problem:
1. Sum the units and amounts across all POs.
2. Write a function to determine the penalty if we ship nothing. Ie, we incur the maximum
penalty possible.
3. Write a function to determine how much of each PO we should fulfill to minimize the
penalty. Calculate the expected penalty with your approach.

Assumptions for parts 3:
A. Assume our inventory available for shipping is 3459 units.
B. You can partially fulfill a PO
C. You may allow for partial units in your allocation solution.
Files
● purchase_orders[.csv|.json] - List of POs
● penalty_rates[.csv|.json] - Target fill rates and penalty for each customer