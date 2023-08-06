from circle.resources.abstract import CreateableAPIResource


class MockWirePayment(CreateableAPIResource):
    OBJECT_NAME = "mocks.payments.wire"
