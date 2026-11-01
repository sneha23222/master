# This program calculates the recruitment fee and GST for a candidate placement.

# from recruitment_lib import calculate_fee, calculate_gst, print_summary

import recruitment_lib as rl

# -------------------------
# Main Program
# -------------------------

def exec_func():
    candidate = "Anita Sharma"
    company = "ABC Technologies"
    salary = 1200000

    # Positional arguments
    recruitment_fee = rl.calculate_fee(
        salary,
        8.33,
        5000
    )

    # Keyword arguments
    gst_amount = rl.calculate_gst(
        amount=recruitment_fee,
        gst_rate=18
    )

    rl.print_summary(
        candidate_name=candidate,
        company_name=company,
        fee=recruitment_fee,
        gst=gst_amount
    )


if __name__ == "__main__":   # This is the entry point of the program.
    exec_func()