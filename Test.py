import pytest
from Window import Window


@pytest.fixture
def app(qtbot):
    testApp = Window()
    qtbot.addWidget(testApp)
    return testApp


@pytest.fixture(scope='function', autouse=True)
def setup(app, request):
    request.instance.app = app


class TestGUI:
    def testFxLineEditHeight(self, request):
        assert request.instance.app.fx.height() == 50

    def testXMinHeight(self, request):
        assert request.instance.app.xmin.height() == 50

    def testXMaxHeight(self, request):
        assert request.instance.app.xmax.height() == 50

    def testFxLineEditFont(self, request):
        assert request.instance.app.fx.font().family() == "Cambria"
        assert request.instance.app.fx.font().pointSize() == 15
        assert request.instance.app.fx.font().weight() == 10
        assert request.instance.app.fx.font().italic() == True

    def testXMinFont(self, request):
        assert request.instance.app.xmin.font().family() == "Cambria"
        assert request.instance.app.xmin.font().pointSize() == 15
        assert request.instance.app.xmin.font().weight() == 10
        assert request.instance.app.xmin.font().italic() == True

    def testXMaxFont(self, request):
        assert request.instance.app.xmax.font().family() == "Cambria"
        assert request.instance.app.xmax.font().pointSize() == 15
        assert request.instance.app.xmax.font().weight() == 10
        assert request.instance.app.xmax.font().italic() == True

    def testPlotButtonFont(self, request):
        assert request.instance.app.plotButton.font().family() == "Cambria"
        assert request.instance.app.plotButton.font().pointSize() == 15
        assert request.instance.app.plotButton.font().weight() == 10
        assert request.instance.app.plotButton.font().italic() == True

    def testPlotButtonHeight(self, request):
        assert request.instance.app.plotButton.height() == 75

    def testFxLabelFont(self, request):
        assert request.instance.app.fxLabel.font().family() == "Cambria"
        assert request.instance.app.fxLabel.font().pointSize() == 15
        assert request.instance.app.fxLabel.font().weight() == 5
        assert request.instance.app.fxLabel.font().italic() == True
    
    def testXMinLabelFont(self, request):
        assert request.instance.app.xminLabel.font().family() == "Cambria"
        assert request.instance.app.xminLabel.font().pointSize() == 15
        assert request.instance.app.xminLabel.font().weight() == 5
        assert request.instance.app.xminLabel.font().italic() == True
    
    def testXMaxLabelFont(self, request):
        assert request.instance.app.xmaxLabel.font().family() == "Cambria"
        assert request.instance.app.xmaxLabel.font().pointSize() == 15
        assert request.instance.app.xmaxLabel.font().weight() == 5
        assert request.instance.app.xmaxLabel.font().italic() == True
    


class TestInputs:
    def testFxLineEditPlaceholder(self, request):
        assert request.instance.app.fx.placeholderText() == "i.e. 9*x^2+6"

    def testXMinRange(self, request):
        assert request.instance.app.xmin.minimum() == -1000000000
        assert request.instance.app.xmin.maximum() == 1000000000

    def testXMaxRange(self, request):
        assert request.instance.app.xmax.minimum() == -1000000000
        assert request.instance.app.xmax.maximum() == 1000000000

    def testXMinDefaultValue(self, request):
        assert request.instance.app.xmin.value() == 0

    def testXMaxDefaultValue(self, request):
        assert request.instance.app.xmax.value() == 1

    def testXMinDecimals(self, request):
        assert request.instance.app.xmin.decimals() == 3

    def testXMaxDecimals(self, request):
        assert request.instance.app.xmax.decimals() == 3

    def testIfAllEditable(self, request):
        assert request.instance.app.fx.isReadOnly() == False
        assert request.instance.app.xmin.isReadOnly() == False
        assert request.instance.app.xmax.isReadOnly() == False

    def testMinXStepUp(self, request):
        request.instance.app.xmin.stepUp()
        assert request.instance.app.xmin.value() == 1

    def testMinXStepDown(self, request):
        request.instance.app.xmin.stepDown()
        assert request.instance.app.xmin.value() == -1

    def testMaxXStepUp(self, request):
        request.instance.app.xmax.stepUp()
        assert request.instance.app.xmax.value() == 2

    def testMaxXStepDown(self, request):
        request.instance.app.xmax.stepDown()
        assert request.instance.app.xmax.value() == 0

    def testEmptyFx(self, request):
        request.instance.app.fx.setText("")
        request.instance.app.xmin.setValue(0)
        request.instance.app.xmax.setValue(1)
        request.instance.app.plotButton.click()
        assert request.instance.app.errorMsg == "f(x) shouldn't be empty"

    def testInvalidFx(self, request):
        request.instance.app.fx.setText("nx+65-")
        request.instance.app.xmin.setValue(0)
        request.instance.app.xmax.setValue(1)
        request.instance.app.plotButton.click()
        assert request.instance.app.errorMsg == "Error while parsing f(x)"

    def testXMinGreaterThanXMax(self, request):
        request.instance.app.fx.setText("x")
        request.instance.app.xmin.setValue(1)
        request.instance.app.xmax.setValue(0)
        request.instance.app.plotButton.click()
        assert request.instance.app.errorMsg == "Xmin should be less than Xmax"

    def testXMinEqualToXMax(self, request):
        request.instance.app.fx.setText("x")
        request.instance.app.xmin.setValue(1)
        request.instance.app.xmax.setValue(1)
        request.instance.app.plotButton.click()
        assert request.instance.app.errorMsg == "Xmin should be less than Xmax"

    def testValidInputs(self, request):
        request.instance.app.fx.setText("3 * x ^ 2 + 3")
        request.instance.app.xmin.setValue(-50.62)
        request.instance.app.xmax.setValue(50.36)
        request.instance.app.plotButton.click()
        assert hasattr(request.instance.app, "errorMsg") == False
