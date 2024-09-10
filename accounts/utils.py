def detecUser(user):
    if user.role ==1:
        redeirectUrl ='RestaurantDashboard'
        return redeirectUrl 

    elif user.role == 2:
        redeirectUrl = 'custDashboard'
        return redeirectUrl 

    elif user.role == None and user.is_superadmin:
        redeirectUrl = '/admin'
        return redeirectUrl 