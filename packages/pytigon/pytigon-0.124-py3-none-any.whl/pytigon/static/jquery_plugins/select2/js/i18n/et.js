/*! Select2 4.1.0-beta.1 | https://github.com/select2/select2/blob/master/LICENSE.md */

!function(){if(jQuery&&jQuery.fn&&jQuery.fn.select2&&jQuery.fn.select2.amd)var e=jQuery.fn.select2.amd;e.define("select2/i18n/et",[],function(){return{inputTooLong:function(e){var n=e.input.length-e.maximum,t="Sisesta "+n+" täht";return 1!=n&&(t+="e"),t+=" vähem"},inputTooShort:function(e){var n=e.minimum-e.input.length,t="Sisesta "+n+" täht";return 1!=n&&(t+="e"),t+=" rohkem"},loadingMore:function(){return"Laen tulemusi…"},maximumSelected:function(e){var n="Saad vaid "+e.maximum+" tulemus";return 1==e.maximum?n+="e":n+="t",n+=" valida"},noResults:function(){return"Tulemused puuduvad"},searching:function(){return"Otsin…"},removeAllItems:function(){return"Eemalda kõik esemed"}}}),e.define,e.require}();