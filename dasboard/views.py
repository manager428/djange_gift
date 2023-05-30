from django.db.models.functions.datetime import Extract
from django.shortcuts import render
from shop.models import OrderProduct, Loginhistory, Product
from django.db.models import Sum
from datetime import date




def dasboard(request):
    today = date.today()
    currentyear = today.strftime("%Y")
    # print("currentyear =", currentyear)
    
    charts_product = OrderProduct.objects.filter(updated_at__year=currentyear).annotate(month=Extract('updated_at', 'month')).values('month').annotate(data_sum=Sum('qty')).order_by('month')
    # print(charts_product)
    
    
    temp_charts_category = OrderProduct.objects.filter(updated_at__year=currentyear).values('product__category_id').annotate(data_sum=Sum('qty')).order_by('-data_sum')
    
    
    buckets = [0] * 12
    for i in range(charts_product.count()):
        index = charts_product[i]['month'] - 1
        buckets[index] = charts_product[i]['data_sum']

    # print(buckets)

    if temp_charts_category.count() > 0:
        max_category_id = temp_charts_category[0]["product__category_id"]
        charts_category = OrderProduct.objects.filter(product__category_id=max_category_id).annotate(month=Extract('updated_at', 'month')).values('month').annotate(data_sum=Sum('qty')).order_by('month')
    # print(max_category_id)
    categorys = [0] * 12
    for i in range(charts_category.count()):
        index = charts_category[i]['month'] - 1
        categorys[index] = charts_category[i]['data_sum']
    sum_order_product = OrderProduct.objects.filter(updated_at__year=currentyear).aggregate(data_sum=Sum('qty'))['data_sum']
    # print(sum_order_product)
    count_category = OrderProduct.objects.filter(updated_at__year=currentyear).values('product__category__category_name').annotate(data_sum=Sum('qty')).order_by('-data_sum')
    for item in count_category:
        item['percent'] = item['data_sum']/sum_order_product* 100

    temp_top_product = OrderProduct.objects.filter(updated_at__year=currentyear).values('product_id').annotate(data_sum=Sum('qty')).order_by('-data_sum')[:10]

    for temp in temp_top_product:
        temp['product'] = Product.objects.get(id=temp["product_id"])

    temp_top_user_product = OrderProduct.objects.filter(updated_at__year=currentyear).values('user_id__username').annotate(data_sum=Sum('qty'), data_amount=Sum('amount')).order_by('-data_sum')
    
    users = Loginhistory.objects.values('user_id', 'user_id__username').order_by('user_id').distinct()
    for temp in users:
        temp["month_vals"] =  Loginhistory.objects.filter(updated_at__year=currentyear, user_id=temp["user_id"]).annotate(month=Extract('updated_at','month')).values('updated_at__month').annotate(logindata_sum=Sum('logindata')).order_by('updated_at__month')
    # print(users)

    temp_use_user_month = Loginhistory.objects.filter(updated_at__year=currentyear).annotate(month=Extract('updated_at','month')).values('updated_at__month', 'user_id__username').annotate(logindata_sum=Sum('logindata')).order_by('updated_at__month')
 

    for temp in users:
        use_user_month = [0] * 12
        for tmp in temp["month_vals"]:
            use_user_month[tmp["updated_at__month"]-1] = tmp["logindata_sum"]
        temp["use_user_month"] = use_user_month
    print(users)
    details = {
        'arr_products': buckets,
        'categorys': categorys,
        'category_id': max_category_id,
        'count_category': count_category,
        'temp_top_product': temp_top_product,
        'temp_top_user_product':temp_top_user_product,
        'users':users,
        }
    return render(request,"dasboard.html", details)
    