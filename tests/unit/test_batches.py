from datetime import date
from src.model import Batch, OrderLine


def make_batch_and_order(sku, batch_qty, line_qty):
    return (
        Batch('batch-001', sku, qty=batch_qty, eta=date.today()),
        OrderLine('order-001', sku, line_qty)
    )


def test_allocating_to_batch_reduces_available_quantity():
    batch, order_line = make_batch_and_order('small table', 20, 2)

    batch.allocate(order_line)

    assert batch.available_quantity == 18


def test_can_allocate_if_available_greater_than_order():
    batch, order_line = make_batch_and_order('Washing machine', 20, 2)

    assert batch.can_allocate(order_line)


def test_can_allocate_if_available_equal_to_order():
    batch, order_line = make_batch_and_order('Sofa', 2, 2)

    assert batch.can_allocate(order_line)


def test_cannot_allocate_if_available_less_than_order():
    batch, order_line = make_batch_and_order('Crockery', 10, 12)

    assert batch.can_allocate(order_line) is False


def test_cannot_allocate_if_sku_doesnt_match():
    batch = Batch('batch-001', 'Wall Clock', qty=10, eta=date.today())
    order_line = OrderLine('order-001', 'Portrait', 3)

    assert batch.can_allocate(order_line) is False


def test_allocation_is_idempotent():
    batch, order_line = make_batch_and_order('small table', 20, 2)

    batch.allocate(order_line)
    batch.allocate(order_line)
    batch.allocate(order_line)

    assert batch.available_quantity == 18


def test_can_only_deallocate_allocated_item():
    batch, unallocated_order_line = make_batch_and_order('Crockery', 10, 2)
    batch.deallocate(unallocated_order_line)

    assert batch.available_quantity == 10


def test_deallocate():
    batch, order_line = make_batch_and_order('Crockery', 15, 2)
    batch.allocate(order_line)
    batch.deallocate(order_line)

    assert batch.available_quantity == 15
