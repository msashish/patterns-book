from datetime import date, timedelta
from src.model import allocate, Batch, OrderLine, OutOfStock
import pytest

today = date.today()
tomorrow = today + timedelta(days=1)
later = tomorrow + timedelta(days=10)


def test_prefers_in_stock_batches_over_shipment():
    in_stock_batch = Batch("in-stock-batch", "RETRO-CLOCK", 100, eta=None)
    shipment_batch = Batch("shipment-batch", "RETRO-CLOCK", 100, eta=tomorrow)
    line = OrderLine("oref", "RETRO-CLOCK", 10)

    allocate(line, [in_stock_batch, shipment_batch])

    assert in_stock_batch.available_quantity == 90
    assert shipment_batch.available_quantity == 100


def test_prefers_earliest_batch():
    earliest_batch = Batch("in-stock-batch", "MINIMALIST-SPOON", 100, eta=today)
    tomorrow_batch = Batch("in-stock-batch", "MINIMALIST-SPOON", 100, eta=tomorrow)
    later_batch = Batch("in-stock-batch", "MINIMALIST-SPOON", 100, eta=later)
    line = OrderLine("oref", "MINIMALIST-SPOON", 10)

    allocate(line, [earliest_batch, tomorrow_batch, later_batch])

    assert earliest_batch.available_quantity == 90
    assert tomorrow_batch.available_quantity == 100
    assert later_batch.available_quantity == 100


def test_allocate_returns_batch_reference():
    in_stock_batch = Batch("in-stock-batch-ref", "HIGHBROW-POSTER", 100, eta=None)
    shipment_batch = Batch("shipment-batch-ref", "HIGHBROW-POSTER", 100, eta=tomorrow)
    line = OrderLine("oref", "HIGHBROW-POSTER", 10)
    allocation = allocate(line, [in_stock_batch, shipment_batch])
    assert allocation == in_stock_batch.reference


def test_raises_out_of_stock_exception_if_cannot_allocate():
    batch = Batch('batch1', 'SMALL-FORK', 10, eta=today)
    allocate(OrderLine('order1', 'SMALL-FORK', 10), [batch])

    with pytest.raises(OutOfStock, match='SMALL-FORK'):
        allocate(OrderLine('order1', 'SMALL-FORK', 1), [batch])
