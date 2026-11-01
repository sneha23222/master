# This program calculates the recruitment fee and GST for a candidate placement.

def calculate_fee(annual_salary, fee_percentage, discount=0):
    base_fee = annual_salary * fee_percentage / 100
    final_fee = base_fee - discount
    return final_fee


def calculate_gst(amount, gst_rate=18):
    gst = amount * gst_rate / 100
    return gst


def print_summary(**kwargs):
    candidate_name = kwargs.get("candidate_name")
    company_name = kwargs.get("company_name")
    fee = kwargs.get("fee")
    gst = kwargs.get("gst")
    total_amount = fee + gst

    print("Placement Summary")
    print("-----------------")
    print("Candidate:", candidate_name)
    print("Company:", company_name)
    print("Recruitment Fee:", fee)
    print("GST:", gst)
    print("Total Invoice:", total_amount)


# -------------------------
# Main Program
# -------------------------

def exec_func():
    candidate = "Anita Sharma"
    company = "ABC Technologies"
    salary = 1200000

    # Positional arguments
    recruitment_fee = calculate_fee(
        salary,
        8.33,
        5000
    )

    # Keyword arguments
    gst_amount = calculate_gst(
        amount=recruitment_fee,
        gst_rate=18
    )

    print_summary(
        candidate_name=candidate,
        company_name=company,
        fee=recruitment_fee,
        gst=gst_amount
    )


if __name__ == "__main__":   # This is the entry point of the program.
    exec_func()