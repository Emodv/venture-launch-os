from intelligence import attribution_label, benchmark_eligible, score_data_quality


def test_gold_standard_case_scores_high() -> None:
    result = score_data_quality(
        {
            "business_context": 1,
            "search_console": 1,
            "analytics": 1,
            "paid_search": 1,
            "landing_page_mapping": 1,
            "strategy_context": 1,
            "outcome_evidence": 1,
            "time_series_depth": 1,
            "cross_source_joinability": 1,
        }
    )
    assert result.total == 100
    assert result.classification == "gold_standard"


def test_partial_case_is_not_benchmark_ready() -> None:
    result = score_data_quality(
        {
            "business_context": 1,
            "search_console": 0.5,
            "analytics": 0.25,
            "paid_search": 0,
            "landing_page_mapping": 0.5,
            "strategy_context": 1,
            "outcome_evidence": 0,
            "time_series_depth": 0.5,
            "cross_source_joinability": 0.25,
        }
    )
    assert result.total < 70
    assert not benchmark_eligible(result.total, 0.9)


def test_benchmark_requires_quality_and_compatibility() -> None:
    assert benchmark_eligible(85, 0.8)
    assert not benchmark_eligible(85, 0.4)
    assert not benchmark_eligible(60, 0.9)


def test_attribution_is_conservative() -> None:
    assert attribution_label(True, True) == "VERIFIED"
    assert attribution_label(False, True) == "STRONGLY_SUPPORTED"
    assert attribution_label(False, False) == "INFERRED"
