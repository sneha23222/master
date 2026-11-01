# This module contains reusable functions for recruitment fee calculations.


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
