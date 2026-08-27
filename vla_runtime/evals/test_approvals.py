from approvals import ApprovalClass, classify_action, may_execute


def test_autonomous_default():
    assert classify_action("research") == ApprovalClass.AUTONOMOUS
    assert may_execute("research") is True


def test_explicit_purchase_blocked():
    assert classify_action("purchase") == ApprovalClass.EXPLICIT_APPROVAL
    assert may_execute("purchase") is False


def test_preauthorized_requires_policy():
    assert classify_action("send_outreach") == ApprovalClass.PREAUTHORIZED
    assert may_execute("send_outreach") is False
    assert may_execute("send_outreach", {"send_outreach"}) is True
