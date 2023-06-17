from . import ct

def design_ct(study_type, age_group, weight_kg, rate_formula="no_delay", delay_sec=None):

    assert study_type in ["chest", "whole_abd", "chest_whole_abd", "cta_liver"], "Invalid study_type argument, Please choose: 'chest', 'whole_abd', 'chest_whole_abd', 'cta_liver'"
    assert age_group in ["younger_child", "older_child"], "Invalid `age_group`, Please choose: 'younger_child' or 'older_child'"
    assert rate_formula in ["no_delay", "delay"], "Invalid rate_formula argument. Please choose 'no_delay' or 'delay'."

    # CT Chest
    if study_type == "chest":
        ct.design_chest(age_group=age_group, weight_kg=weight_kg)
    
    # CT Whole Abdomen
    if study_type == "whole_abd":
        ct.design_whole_abd(age_group=age_group, weight_kg=weight_kg, rate_formula=rate_formula, delay_sec=delay_sec)
    
    # CT Chest + WA
    if study_type == "chest_whole_abd":
        ct.design_chest_whole_abd(age_group=age_group, weight_kg=weight_kg, rate_formula=rate_formula, delay_sec=delay_sec)
    
    # CTA Liver
    if study_type == "cta_liver":
        ct.design_cta_liver(age_group=age_group, weight_kg=weight_kg)

# For Testing
if __name__ == "__main__":
    design_ct("chest", "younger_child", 3)