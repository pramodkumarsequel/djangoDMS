
        
//creates custom alert object
var custom_alert = new custom_alert();

function updateElementIndex(el, prefix, ndx) {
    var id_regex = new RegExp('(' + prefix + '-\\d+)');
    var replacement = prefix + '-' + ndx;
    if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
    if (el.id) el.id = el.id.replace(id_regex, replacement);
    if (el.name) el.name = el.name.replace(id_regex, replacement);
}

//stores the total no of item forms
var total = 1;

function cloneMore(selector, prefix) {
    var newElement = $(selector).clone(true);
    //var total = $('#id_' + prefix + '-TOTAL_FORMS').val();
    newElement.find(':input:not([type=button]):not([type=submit]):not([type=reset])').each(function() {
        var name = $(this).attr('name')
        if(name) {
            name = name.replace('-' + (total-1) + '-', '-' + total + '-');
            var id = 'id_' + name;
            $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
        }
    });
    newElement.find('label').each(function() {
        var forValue = $(this).attr('for');
        if (forValue) {
        forValue = forValue.replace('-' + (total-1) + '-', '-' + total + '-');
        $(this).attr({'for': forValue});
        }
    });
    total++;
    $('#id_' + prefix + '-TOTAL_FORMS').val(total);
    $(selector).after(newElement);
    return false;
}

function deleteForm(prefix, btn) {
    //var total = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    if (total > 1){
        btn.closest('.form-row').remove();
        var forms = $('.form-row');
        $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
        for (var i=0, formCount=forms.length; i<formCount; i++) {
            $(forms.get(i)).find(':input').each(function() {
                updateElementIndex(this, prefix, i);
            });
        }
        total--;
    } else {
        custom_alert.render('Field cannot be deleted');
    }
    return false;
}

$(document).on('click', '.add-form-row', function(e){
    e.preventDefault();
    cloneMore("table tr:last", "form");
    return false;
});

$(document).on('click', '.remove-form-row', function(e){
    e.preventDefault();
    deleteForm('form', $(this));
    return false;
});


//stores pk and quantity of all stocks into a js object 'stocks'
var stocks = [
    {% for stock in stocks %}
        {% if not forloop.first %},{% endif %}
        {
            pk          : {{ stock.pk }},
            quantity    : {{ stock.quantity }}
        }
    {% endfor %}
];

//updates the total price by multiplying 'price per item' and 'quantity' 
$(document).on('change', '.setprice', function(e){
    e.preventDefault();
    //gets the values
    var element = $(this);
    var stock = element.parents('.form-row').find('.stock').val();
    var quantity = element.parents('.form-row').find('.quantity').val();
    var perprice = element.parents('.form-row').find('.price').val();
    //checks if stocks are available
    stocks.forEach(function(stockSummary, i) {
        var pk = stocks[i].pk;
        var squantity = stocks[i].quantity;
        if(stock == pk) {
            //checks if ordered stock is more than available stock
            if(quantity > squantity){
                quantity = quantity - 1;
                if(quantity <= 1){
                    //no stocks are available. Attempts to delete field
                    custom_alert.render('Stocks are currently unavailable. Field will be removed;');
                    //Sets quantity to 0 as failsafe for when the total no of item forms are 1
                    element.parents('.form-row').find('.quantity').val(0);
                    deleteForm('form', element);
                } else {
                    element.parents('.form-row').find('.quantity').val(squantity-1);
                    quantity = squantity - 1;
                    custom_alert.render('Exceeded current stock available');
                }
            }
        }
    });     
    //calculates the total
    var tprice = quantity * perprice;
    //sets it to field
    element.parents('.form-row').find('.totalprice').val(tprice);
    return false;
});

