/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 357);
/******/ })
/************************************************************************/
/******/ ({

/***/ 100:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/wizard/examples.html");

/***/ }),

/***/ 24:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
// ESM COMPAT FLAG
__webpack_require__.r(__webpack_exports__);

// CONCATENATED MODULE: ./src/components/swipe/swipe.js
class SwipeEventDispatcher {
  constructor(element, options = {}) {
    this.evtMap = {
      SWIPE_DOWN: [],
      SWIPE_LEFT: [],
      SWIPE_RIGHT: [],
      SWIPE_UP: [],
    }
    this.xDown = null
    this.yDown = null
    this.element = element
    this.options = Object.assign({ triggerPercent: 0.3 }, options)
    element.addEventListener(
      'touchstart',
      (evt) => {
        return this.handleTouchStart(evt)
      },
      false
    )
    element.addEventListener(
      'touchend',
      (evt) => {
        return this.handleTouchEnd(evt)
      },
      false
    )
  }

  on(evt, cb) {
    this.evtMap[evt].push(cb)
  }

  off(evt, lcb) {
    this.evtMap[evt] = this.evtMap[evt].filter((cb) => {
      return cb !== lcb
    })
  }

  trigger(evt, data) {
    this.evtMap[evt].map((handler) => {
      return handler(data)
    })
  }

  handleTouchStart(evt) {
    this.xDown = evt.touches[0].clientX
    this.yDown = evt.touches[0].clientY
  }

  handleTouchEnd(evt) {
    const deltaX = evt.changedTouches[0].clientX - this.xDown
    const deltaY = evt.changedTouches[0].clientY - this.yDown
    const distMoved = Math.abs(
      Math.abs(deltaX) > Math.abs(deltaY) ? deltaX : deltaY
    )
    const activePct = distMoved / this.element.offsetWidth
    if (activePct > this.options.triggerPercent) {
      if (Math.abs(deltaX) > Math.abs(deltaY)) {
        deltaX < 0 ? this.trigger('SWIPE_LEFT') : this.trigger('SWIPE_RIGHT')
      } else {
        deltaY > 0 ? this.trigger('SWIPE_DOWN') : this.trigger('SWIPE_UP')
      }
    }
  }
}
/* harmony default export */ var swipe = (SwipeEventDispatcher);

// CONCATENATED MODULE: ./src/components/wizard/wizard.js

class wizard_BRWizard {
  constructor(name, component) {
    this.name = name
    this.component = component
    // DOM elements
    this.DOMstrings = {
      stepFormPanelClass: 'wizard-panel',
      // stepFormPanels: document.querySelectorAll('.wizard-panel'),
      stepFormPanels: this.component.querySelectorAll('.wizard-panel'),
      stepNextBtnClass: 'wizard-btn-next',
      stepPrevBtnClass: 'wizard-btn-prev',
      // stepsBar: document.querySelector('.wizard-progress'),
      stepsBar: this.component.querySelector('.wizard-progress'),
      stepsBarClass: 'wizard-progress',
      stepsBtnClass: 'wizard-progress-btn',
      // stepsBtns: document.querySelectorAll(`.wizard-progress-btn`),
      stepsBtns: this.component.querySelectorAll('.wizard-progress-btn'),
      // stepsForm: document.querySelector('.wizard-form'),
      stepsForm: this.component.querySelector('.wizard-form'),
    }
    // remove class from a set of items
    this.removeAttributes = (elemSet, attrName) => {
      elemSet.forEach((elem) => {
        elem.removeAttribute(attrName)
      })
    }
    // return exect parent node of the element
    this.findParent = (elem, parentClass) => {
      let currentNode = elem
      while (!currentNode.classList.contains(parentClass)) {
        currentNode = currentNode.parentNode
      }
      return currentNode
    }
    // get active button step number
    this.getActiveStep = (elem) => {
      return Array.from(this.DOMstrings.stepsBtns).indexOf(elem)
    }
    // set all steps before clicked (and clicked too) to active
    this.setActiveStep = (activeStepNum) => {
      // remove active state from all the state
      this.removeAttributes(this.DOMstrings.stepsBtns, 'active')
      // this.removeAttributes(this.DOMstrings.stepsBtns, 'disabled')

      // set picked items to active
      this.DOMstrings.stepsBtns.forEach((elem, index) => {
        if (index === activeStepNum) {
          elem.removeAttribute('disabled')
          elem.setAttribute('active', '')
        }
        // if (index > activeStepNum) {
        //   elem.setAttribute('disabled', 'disabled')
        // }
      })
    }
    // get active panel
    this.getActivePanel = () => {
      let activePanel
      this.DOMstrings.stepFormPanels.forEach((elem) => {
        if (elem.hasAttribute('active')) {
          activePanel = elem
        }
      })
      return activePanel
    }
    // open active panel (and close unactive panels)
    this.setActivePanel = (activePanelNum) => {
      // remove active class from all the panels
      this.removeAttributes(this.DOMstrings.stepFormPanels, 'active')
      // show active panel
      this.DOMstrings.stepFormPanels.forEach((elem, index) => {
        if (index === activePanelNum) {
          elem.setAttribute('active', '')
        }
      })
    }
    this.setStepsNum = () => {
      this.DOMstrings.stepsBtns.forEach((elem, index) => {
        elem.setAttribute('step', index + 1)
      })
    }
    this.setStep = (num) => {
      const activeStep = num <= this.DOMstrings.stepsBtns.length ? num - 1 : 0
      this.setActiveStep(activeStep)
      this.setActivePanel(activeStep)
    }
    this.collapseSteps = () => {
      this.component.setAttribute('collapsed', '')
    }
    this.expandSteps = () => {
      this.component.removeAttribute('collapsed')
    }
    this._setBehavior()
  }

  _setBehavior() {
    // STEPS BAR CLICK FUNCTION
    this.DOMstrings.stepsBar.addEventListener('click', (e) => {
      // check if click target is a step button
      const eventTarget = e.target
      if (!eventTarget.classList.contains(`${this.DOMstrings.stepsBtnClass}`)) {
        e.target.parentNode.click()
        return
      }
      // get active button step number
      const activeStep = this.getActiveStep(eventTarget)
      // set all steps before clicked (and clicked too) to active
      this.setActiveStep(activeStep)
      // open active panel
      this.setActivePanel(activeStep)
    })
    // PREV/NEXT BTNS CLICK
    this.DOMstrings.stepsForm.addEventListener('click', (e) => {
      const eventTarget = e.target
      // check if we clicked on `PREV` or NEXT` buttons
      if (
        !(
          eventTarget.classList.contains(
            `${this.DOMstrings.stepPrevBtnClass}`
          ) ||
          eventTarget.classList.contains(`${this.DOMstrings.stepNextBtnClass}`)
        )
      ) {
        return
      }
      // find active panel
      const activePanel = this.findParent(
        eventTarget,
        `${this.DOMstrings.stepFormPanelClass}`
      )
      let activePanelNum = Array.from(this.DOMstrings.stepFormPanels).indexOf(
        activePanel
      )
      // set active step and active panel onclick
      if (
        eventTarget.classList.contains(`${this.DOMstrings.stepPrevBtnClass}`)
      ) {
        activePanelNum -= 1
        activePanel.style.left = '1%'
      } else {
        activePanelNum += 1
        activePanel.style.left = '-1%'
      }
      this.setActiveStep(activePanelNum)
      this.setActivePanel(activePanelNum)
    })
    // Set Steps label number
    this.setStepsNum()
    // Set default active step
    if (this.component.hasAttribute('step')) {
      this.setStep(this.component.getAttribute('step'))
    }
    // set steps buttons grid style if it needs to scroll horizontaly
    if (
      this.component.hasAttribute('scroll') &&
      !this.component.hasAttribute('vertical')
    ) {
      const stepsWidth =
        Math.round(100 / this.DOMstrings.stepsBtns.length) - 0.5
      this.DOMstrings.stepsBar.style.gridTemplateColumns = `repeat(auto-fit, minmax(100px, ${stepsWidth}% ))`
    }
    // Swipe
    const dispatcher = new swipe(this.DOMstrings.stepsBar)
    if (this.component.hasAttribute('vertical')) {
      dispatcher.on('SWIPE_LEFT', () => {
        this.collapseSteps()
      })
      dispatcher.on('SWIPE_RIGHT', () => {
        this.expandSteps()
      })
      this.DOMstrings.stepsForm.ontouchstart = () => {
        this.collapseSteps()
      }
    } else {
      this.DOMstrings.stepsBar.ontouchstart = () => {
        this.expandSteps()
      }
      this.DOMstrings.stepsForm.ontouchstart = () => {
        this.collapseSteps()
      }
    }
  }
}
const wizardList = []
for (const brWizard of window.document.querySelectorAll('.br-wizard')) {
  wizardList.push(new wizard_BRWizard('br-wizard', brWizard))
}
/* harmony default export */ var wizard = __webpack_exports__["default"] = (wizard_BRWizard);


/***/ }),

/***/ 357:
/***/ (function(module, exports, __webpack_require__) {

__webpack_require__(24);
__webpack_require__(99);
__webpack_require__(100);
__webpack_require__(358);
module.exports = __webpack_require__(359);


/***/ }),

/***/ 358:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/wizard/examples/wizard-horizontal.html");

/***/ }),

/***/ 359:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/wizard/examples/wizard-vertical.html");

/***/ }),

/***/ 99:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
// extracted by mini-css-extract-plugin


/***/ })

/******/ });
//# sourceMappingURL=wizard.js.map