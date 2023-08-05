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
/******/ 	return __webpack_require__(__webpack_require__.s = 146);
/******/ })
/************************************************************************/
/******/ ({

/***/ 146:
/***/ (function(module, exports, __webpack_require__) {

__webpack_require__(9);
__webpack_require__(43);
__webpack_require__(44);
__webpack_require__(147);
__webpack_require__(148);
__webpack_require__(149);
__webpack_require__(150);
module.exports = __webpack_require__(151);


/***/ }),

/***/ 147:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/card/examples/card-completo.html");

/***/ }),

/***/ 148:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/card/examples/card-desativado.html");

/***/ }),

/***/ 149:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/card/examples/card-expansao.html");

/***/ }),

/***/ 150:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/card/examples/card-flip.html");

/***/ }),

/***/ 151:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/card/examples/card-simples.html");

/***/ }),

/***/ 43:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
// extracted by mini-css-extract-plugin


/***/ }),

/***/ 44:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/card/examples.html");

/***/ }),

/***/ 9:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
class BRCard {
  constructor(name, component, id) {
    this.name = name
    this.component = component
    this.component.setAttribute('id', `card${id}`)
    this._setBehavior()
    new BRCardFlip()
    new BRCardCollapse()
  }

  _setBehavior() {
    this._setFlipBehavior()
    this._setExpandBehavior()
    this._setDragBehavior()
  }

  _setFlipBehavior() {
    for (const flip of this.component.querySelectorAll('button.flip')) {
      flip.addEventListener('click', () => {
        if (this.component.getAttribute('flipped') === 'off') {
          this.component.setAttribute('flipped', 'on')
        } else {
          this.component.setAttribute('flipped', 'off')
        }
      })
    }
  }

  _setExpandBehavior() {
    for (const expand of this.component.querySelectorAll('button.expand')) {
      expand.addEventListener('click', () => {
        if (this.component.getAttribute('expanded') === 'off') {
          this.component.setAttribute('expanded', 'on')
        } else {
          this.component.setAttribute('expanded', 'off')
        }
      })
    }
  }

  _setDragBehavior() {
    for (const img of this.component.querySelectorAll('img')) {
      img.setAttribute('draggable', 'false')
    }
    for (const link of this.component.querySelectorAll('a')) {
      link.setAttribute('draggable', 'false')
    }
    this.component.addEventListener('dragstart', (event) => {
      event.stopPropagation()
      event.dataTransfer.setData(
        'text/plain',
        this.component.getAttribute('id')
      )
      event.dropEffect = 'move'
    })
  }
}

class BRCardFlip {
  constructor() {
    this._setBehavior()
  }

  _setBehavior() {
    const cardFlippers = document.querySelectorAll('.br-card[data-flip]')

    for (const cardFlip of cardFlippers) {
      const cardFront = cardFlip.querySelector('.front')
      const cardBack = cardFlip.querySelector('.back')
      const cardFrontTrigger = cardFlip.querySelector(
        '.front [data-toggle="flip"]'
      )
      const cardBackTrigger = cardFlip.querySelector(
        '.back [data-toggle="flip"]'
      )
      this._cardFlipInit(cardFront, cardBack, cardFrontTrigger, cardBackTrigger)
      this._setCardFrontTrigger(
        cardFrontTrigger,
        cardFront,
        cardBack,
        cardBackTrigger
      )
      this._setCardBackTrigger(
        cardBackTrigger,
        cardFront,
        cardBack,
        cardFrontTrigger
      )
    }
  }

  _setCardFrontTrigger(cardFrontTrigger, cardFront, cardBack, cardBackTrigger) {
    cardFrontTrigger.addEventListener('click', () => {
      return this._cardFlipShowBack(
        cardFront,
        cardBack,
        cardFrontTrigger,
        cardBackTrigger
      )
    })
  }

  _setCardBackTrigger(cardBackTrigger, cardFront, cardBack, cardFrontTrigger) {
    cardBackTrigger.addEventListener('click', () => {
      return this._cardFlipShowFront(
        cardFront,
        cardBack,
        cardFrontTrigger,
        cardBackTrigger
      )
    })
  }

  _cardFlipInit(cardFront, cardBack, cardFrontTrigger, cardBackTrigger) {
    this._cardFlipShowFront(
      cardFront,
      cardBack,
      cardFrontTrigger,
      cardBackTrigger
    )
  }

  _cardFlipShowFront(cardFront, cardBack, cardFrontTrigger, cardBackTrigger) {
    cardFront.removeAttribute('hidden')
    cardFront.setAttribute('aria-hidden', 'false')
    cardFrontTrigger.setAttribute('aria-expanded', 'true')
    cardBack.setAttribute('aria-hidden', 'true')
    cardBack.setAttribute('hidden', '')
    cardBackTrigger.setAttribute('aria-expanded', 'false')
  }

  _cardFlipShowBack(cardFront, cardBack, cardFrontTrigger, cardBackTrigger) {
    cardFront.setAttribute('hidden', '')
    cardFront.setAttribute('aria-hidden', 'true')
    cardFrontTrigger.setAttribute('aria-expanded', 'false')
    cardBack.removeAttribute('hidden')
    cardBack.setAttribute('aria-hidden', 'false')
    cardBackTrigger.setAttribute('aria-expanded', 'true')
  }
}

class BRCardCollapse {
  constructor() {
    this._setBehavior()
  }

  _setBehavior() {
    // Padrão de toggle no card
    const cardToggler = document.querySelector('[data-toggle="collapse"]')
    if (cardToggler !== null) {
      const cardTogglerTarget = document.querySelector(
        cardToggler.dataset.target
      )
      this._cardCollapseInit(cardToggler, cardTogglerTarget)
      cardToggler.addEventListener('click', () => {
        if (cardToggler.getAttribute('aria-expanded') === 'true') {
          this._cardHiddenContent(cardToggler, cardTogglerTarget)
        } else {
          this._cardShowContent(cardToggler, cardTogglerTarget)
        }
      })
    }
  }

  _cardShowContent(cardToggler, cardTogglerTarget) {
    cardToggler.setAttribute('aria-expanded', 'true')
    cardTogglerTarget.setAttribute('aria-hidden', 'true')
    cardTogglerTarget.removeAttribute('hidden')
  }

  _cardHiddenContent(cardToggler, cardTogglerTarget) {
    cardToggler.setAttribute('aria-expanded', 'false')
    cardTogglerTarget.setAttribute('aria-hidden', 'false')
    cardTogglerTarget.setAttribute('hidden', '')
  }

  _cardCollapseInit(cardToggler, cardTogglerTarget) {
    if (cardToggler.dataset.visible) {
      if (cardToggler.dataset.visible === 'true') {
        this._cardShowContent(cardToggler, cardTogglerTarget)
      } else {
        this._cardHiddenContent(cardToggler, cardTogglerTarget)
      }
    } else {
      this._cardHiddenContent(cardToggler, cardTogglerTarget)
    }
  }
}

const listCard = []
for (const [index, brCard] of window.document
  .querySelectorAll('.br-card')
  .entries()) {
  listCard.push(new BRCard('br-card', brCard, index))
}

/* harmony default export */ __webpack_exports__["default"] = (BRCard);


/***/ })

/******/ });
//# sourceMappingURL=card.js.map