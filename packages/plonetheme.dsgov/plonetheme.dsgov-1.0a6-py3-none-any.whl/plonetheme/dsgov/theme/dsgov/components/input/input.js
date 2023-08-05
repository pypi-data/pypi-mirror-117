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
/******/ 	return __webpack_require__(__webpack_require__.s = 185);
/******/ })
/************************************************************************/
/******/ ({

/***/ 12:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
class BRInput {
  constructor(name, component) {
    this.name = name
    this.component = component
    this._currentFocus = -1
    this._setBehavior()
  }

  _setBehavior() {
    this._setPasswordViewBehavior()
    this._setAutocompleteBehavior()
  }

  _setPasswordViewBehavior() {
    for (const inputPassword of this.component.querySelectorAll(
      'input[type="password"]'
    )) {
      if (!inputPassword.disabled) {
        for (const buttonIcon of inputPassword.parentNode.querySelectorAll(
          'button.icon'
        )) {
          buttonIcon.addEventListener(
            'click',
            (event) => {
              this._toggleShowPassword(event)
            },
            false
          )
        }
      }
    }
  }

  _toggleShowPassword(event) {
    for (const icon of event.currentTarget.querySelectorAll(
      '.svg-inline--fa'
    )) {
      if (icon.classList.contains('fa-eye')) {
        icon.classList.remove('fa-eye')
        icon.classList.add('fa-eye-slash')
        for (const input of this.component.querySelectorAll(
          'input[type="password"]'
        )) {
          input.setAttribute('type', 'text')
        }
      } else if (icon.classList.contains('fa-eye-slash')) {
        icon.classList.remove('fa-eye-slash')
        icon.classList.add('fa-eye')
        for (const input of this.component.querySelectorAll(
          'input[type="text"]'
        )) {
          input.setAttribute('type', 'password')
        }
      }
    }
  }

  _setAutocompleteBehavior() {
    for (const inputAutocomplete of this.component.querySelectorAll(
      'input.search-autocomplete'
    )) {
      inputAutocomplete.addEventListener(
        'input',
        (event) => {
          this._clearSearchItems()
          this._buildSearchItems(event.currentTarget)
        },
        false
      )
      inputAutocomplete.addEventListener(
        'keydown',
        (event) => {
          this._handleArrowKeys(event)
        },
        false
      )
    }
  }

  _buildSearchItems(element) {
    const searchList = window.document.createElement('div')
    searchList.setAttribute('class', 'search-items')
    this.component.appendChild(searchList)
    if (element.value !== '') {
      for (const data of this.dataList) {
        if (
          data.substr(0, element.value.length).toUpperCase() ===
          element.value.toUpperCase()
        ) {
          const item = window.document.createElement('div')
          item.innerHTML = `<strong>${data.substr(
            0,
            element.value.length
          )}</strong>`
          item.innerHTML += data.substr(element.value.length)
          item.innerHTML += `<input type="hidden" value="${data}">`
          item.addEventListener(
            'click',
            (event) => {
              for (const input of event.currentTarget.querySelectorAll(
                'input[type="hidden"]'
              )) {
                element.value = input.value
              }
              this._clearSearchItems()
            },
            false
          )
          searchList.appendChild(item)
        }
      }
    } else {
      this._clearSearchItems()
    }
  }

  _clearSearchItems() {
    for (const searchItems of this.component.querySelectorAll(
      '.search-items'
    )) {
      for (const item of searchItems.querySelectorAll('div')) {
        searchItems.removeChild(item)
      }
      this.component.removeChild(searchItems)
    }
  }

  _handleArrowKeys(event) {
    switch (event.keyCode) {
      case 13:
        if (this._currentFocus > -1) {
          event.preventDefault()
          for (const searchItems of this.component.querySelectorAll(
            '.search-items'
          )) {
            for (const itemActive of searchItems.querySelectorAll(
              'div.is-active'
            )) {
              itemActive.click()
            }
          }
          this._currentFocus = -1
        }
        break
      case 38:
        if (this._currentFocus > 0) {
          this._currentFocus -= 1
        }
        this._switchFocus()
        break
      case 40:
        for (const searchItems of this.component.querySelectorAll(
          '.search-items'
        )) {
          if (
            this._currentFocus <
            searchItems.querySelectorAll('div').length - 1
          ) {
            this._currentFocus += 1
          }
        }
        this._switchFocus()
        break
      default:
        break
    }
  }

  _switchFocus() {
    for (const searchItems of this.component.querySelectorAll(
      '.search-items'
    )) {
      for (const [index, item] of searchItems
        .querySelectorAll('div')
        .entries()) {
        if (index === this._currentFocus) {
          item.classList.add('is-active')
        }
        if (index !== this._currentFocus) {
          item.classList.remove('is-active')
        }
      }
    }
  }

  setAutocompleteData(dataList) {
    this.dataList = dataList
  }
}
const countries = [
  'Afeganistão',
  'África do Sul',
  'Albânia',
  'Alemanha',
  'Andorra',
  'Angola',
  'Anguilla',
  'Antártida',
  'Antígua e Barbuda',
  'Antilhas Holandesas',
  'Arábia Saudita',
  'Argélia',
  'Argentina',
  'Armênia',
  'Aruba',
  'Austrália',
  'Áustria',
  'Azerbaijão',
  'Bahamas',
  'Bahrein',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Bélgica',
  'Belize',
  'Benin',
  'Bermudas',
  'Bolívia',
  'Bósnia-Herzegóvina',
  'Botsuana',
  'Brasil',
  'Brunei',
  'Bulgária',
  'Burkina Fasso',
  'Burundi',
  'Butão',
  'Cabo Verde',
  'Camarões',
  'Camboja',
  'Canadá',
  'Cazaquistão',
  'Chade',
  'Chile',
  'China',
  'Chipre',
  'Cingapura',
  'Colômbia',
  'Congo',
  'Coréia do Norte',
  'Coréia do Sul',
  'Costa do Marfim',
  'Costa Rica',
  'Croácia (Hrvatska)',
  'Cuba',
  'Dinamarca',
  'Djibuti',
  'Dominica',
  'Egito',
  'El Salvador',
  'Emirados Árabes Unidos',
  'Equador',
  'Eritréia',
  'Eslováquia',
  'Eslovênia',
  'Espanha',
  'Estados Unidos',
  'Estônia',
  'Etiópia',
  'Fiji',
  'Filipinas',
  'Finlândia',
  'França',
  'Gabão',
  'Gâmbia',
  'Gana',
  'Geórgia',
  'Gibraltar',
  'Grã-Bretanha (Reino Unido, UK)',
  'Granada',
  'Grécia',
  'Groelândia',
  'Guadalupe',
  'Guam (Território dos Estados Unidos)',
  'Guatemala',
  'Guernsey',
  'Guiana',
  'Guiana Francesa',
  'Guiné',
  'Guiné Equatorial',
  'Guiné-Bissau',
  'Haiti',
  'Holanda',
  'Honduras',
  'Hong Kong',
  'Hungria',
  'Iêmen',
  'Ilha Bouvet (Território da Noruega)',
  'Ilha do Homem',
  'Ilha Natal',
  'Ilha Pitcairn',
  'Ilha Reunião',
  'Ilhas Aland',
  'Ilhas Cayman',
  'Ilhas Cocos',
  'Ilhas Comores',
  'Ilhas Cook',
  'Ilhas Faroes',
  'Ilhas Falkland (Malvinas)',
  'Ilhas Geórgia do Sul e Sandwich do Sul',
  'Ilhas Heard e McDonald (Território da Austrália)',
  'Ilhas Marianas do Norte',
  'Ilhas Marshall',
  'Ilhas Menores dos Estados Unidos',
  'Ilhas Norfolk',
  'Ilhas Seychelles',
  'Ilhas Solomão',
  'Ilhas Svalbard e Jan Mayen',
  'Ilhas Tokelau',
  'Ilhas Turks e Caicos',
  'Ilhas Virgens (Estados Unidos)',
  'Ilhas Virgens (Inglaterra)',
  'Ilhas Wallis e Futuna',
  'índia',
  'Indonésia',
  'Irã',
  'Iraque',
  'Irlanda',
  'Islândia',
  'Israel',
  'Itália',
  'Jamaica',
  'Japão',
  'Jersey',
  'Jordânia',
  'Kênia',
  'Kiribati',
  'Kuait',
  'Laos',
  'Látvia',
  'Lesoto',
  'Líbano',
  'Libéria',
  'Líbia',
  'Liechtenstein',
  'Lituânia',
  'Luxemburgo',
  'Macau',
  'Macedônia (República Yugoslava)',
  'Madagascar',
  'Malásia',
  'Malaui',
  'Maldivas',
  'Mali',
  'Malta',
  'Marrocos',
  'Martinica',
  'Maurício',
  'Mauritânia',
  'Mayotte',
  'México',
  'Micronésia',
  'Moçambique',
  'Moldova',
  'Mônaco',
  'Mongólia',
  'Montenegro',
  'Montserrat',
  'Myanma',
  'Namíbia',
  'Nauru',
  'Nepal',
  'Nicarágua',
  'Níger',
  'Nigéria',
  'Niue',
  'Noruega',
  'Nova Caledônia',
  'Nova Zelândia',
  'Omã',
  'Palau',
  'Panamá',
  'Papua-Nova Guiné',
  'Paquistão',
  'Paraguai',
  'Peru',
  'Polinésia Francesa',
  'Polônia',
  'Porto Rico',
  'Portugal',
  'Qatar',
  'Quirguistão',
  'República Centro-Africana',
  'República Democrática do Congo',
  'República Dominicana',
  'República Tcheca',
  'Romênia',
  'Ruanda',
  'Rússia (antiga URSS) - Federação Russa',
  'Saara Ocidental',
  'Saint Vincente e Granadinas',
  'Samoa Americana',
  'Samoa Ocidental',
  'San Marino',
  'Santa Helena',
  'Santa Lúcia',
  'São Bartolomeu',
  'São Cristóvão e Névis',
  'São Martim',
  'São Tomé e Príncipe',
  'Senegal',
  'Serra Leoa',
  'Sérvia',
  'Síria',
  'Somália',
  'Sri Lanka',
  'St. Pierre and Miquelon',
  'Suazilândia',
  'Sudão',
  'Suécia',
  'Suíça',
  'Suriname',
  'Tadjiquistão',
  'Tailândia',
  'Taiwan',
  'Tanzânia',
  'Território Britânico do Oceano índico',
  'Territórios do Sul da França',
  'Territórios Palestinos Ocupados',
  'Timor Leste',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunísia',
  'Turcomenistão',
  'Turquia',
  'Tuvalu',
  'Ucrânia',
  'Uganda',
  'Uruguai',
  'Uzbequistão',
  'Vanuatu',
  'Vaticano',
  'Venezuela',
  'Vietnã',
  'Zâmbia',
  'Zimbábue',
]
const inputList = []
for (const brInput of window.document.querySelectorAll('.br-input')) {
  inputList.push(new BRInput('br-input', brInput))
}
for (const brInput of inputList) {
  brInput.component
    .querySelectorAll('input.search-autocomplete')
    .forEach(() => {
      brInput.setAutocompleteData(countries)
    })
}
/* harmony default export */ __webpack_exports__["default"] = (BRInput);


/***/ }),

/***/ 185:
/***/ (function(module, exports, __webpack_require__) {

__webpack_require__(12);
__webpack_require__(57);
__webpack_require__(58);
__webpack_require__(186);
__webpack_require__(187);
__webpack_require__(188);
__webpack_require__(189);
__webpack_require__(190);
__webpack_require__(191);
__webpack_require__(192);
__webpack_require__(193);
__webpack_require__(194);
module.exports = __webpack_require__(195);


/***/ }),

/***/ 186:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/input/examples/input-cpf-danger.html");

/***/ }),

/***/ 187:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/input/examples/input-cpf-disabled.html");

/***/ }),

/***/ 188:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/input/examples/input-cpf-info.html");

/***/ }),

/***/ 189:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/input/examples/input-cpf-success.html");

/***/ }),

/***/ 190:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/input/examples/input-cpf-warning.html");

/***/ }),

/***/ 191:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/input/examples/input-densidade-alta.html");

/***/ }),

/***/ 192:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/input/examples/input-densidade-baixa.html");

/***/ }),

/***/ 193:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/input/examples/input-densidade-media.html");

/***/ }),

/***/ 194:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/input/examples/input-filtro.html");

/***/ }),

/***/ 195:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/input/examples/input-senha.html");

/***/ }),

/***/ 57:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
// extracted by mini-css-extract-plugin


/***/ }),

/***/ 58:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.p + "components/input/examples.html");

/***/ })

/******/ });
//# sourceMappingURL=input.js.map