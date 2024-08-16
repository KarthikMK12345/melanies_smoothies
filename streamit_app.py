# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
#from snowflake.snowpark.context import get_active_session
cnx=st.connection("snowflake")
session=cnx.session()

# Write directly to the app
st.title(":cup_with_straw: Customize your smoothie :cup_with_straw:")
st.write(
    """Replace this example with your own code!
    **And if you're new to Streamlit,** check
    out our easy-to-follow guides at
    [docs.streamlit.io](https://docs.streamlit.io).
    """
)




session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

name_on_order=st.text_input("Please, enter your name")
st.write("Your name is:",name_on_order)

ingredient_list=st.multiselect('Choose upto 5 ingredients',my_dataframe,max_selections=5)
ingredients_string=''
if ingredient_list:#INGREDIENTS
    
    for each_fruit in ingredient_list:
             ingredients_string+=each_fruit+' '

    st.write(ingredients_string)


my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','"""+name_on_order+"""')"""

#st.write(my_insert_stmt)

time_to_insert=st.button('Submit order')

if time_to_insert:
    session.sql(my_insert_stmt).collect()
    st.success('Your Smoothie is ordered!, '+name_on_order, icon="✅")



