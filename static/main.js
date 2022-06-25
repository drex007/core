console.log("Hello");
const cols = document.querySelector('#cars');
const selection = document.querySelector('#mycarlist');
  
    $.ajax({
        type: 'GET',
        url: '/cols/',
        success: function(response){
            console.log(response.data)
            colsData = response.data
            colsData.map(item=>{
                const option = document.createElement('div')
                option.textContent = item.name
                option.setAttribute('class', 'item')
                option.setAttribute('data-value', item.name)
                option.setAttribute('id', item.id)
                selection.appendChild(option)


            })
        },
        error: function(error){
            console.log(error)
        }

    })

    cols.addEventListener('change', e=>{
        
        const selectedCol = e.target.value;
        console.log(selectedCol);
        $.ajax({
            type: 'GET',
            url:`branches/${selectedCol}/`,
            success: function(response){
                console.log(response)
            },
            error: function(error){
                console.log(error)
            }
        })
    })