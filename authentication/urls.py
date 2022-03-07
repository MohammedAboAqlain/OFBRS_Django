from django.urls import path
from knox import views as knox_views
from authentication.views import (
                    LoginAPI,
                    IndexMarket,
                    AllSeller,
                    AllSellerByMarket,
                    AllFisherman,
                    DeleteMarket,
                    AddEntry,
                    AddUser,
                    AddStorageEntry,
                    UpdateUserName,
                    UpdateUserPhone,
                    UpdateUserMarket,
                    CreateMarket,
                    UpdateEntryQuantity,
                    reset_broken,
                    reset_lost,
                    deactivate_user_status,
                    reactivate_user_status,
                    delete_user,
                    delete_entry,
                    delete_storage_entry,
                    AllFAQs,
                    get_storage_balance,
                    get_number_manufactured,
                    GetEntryType,
                    GetEntryTypeObject,
                    AllDeletedUsers,
                    get_calculate_lost,
                    AllStorageEntries,
                    get_broken,
                    RegisterAPI,
                    )

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view()),
#     path('logout/', knox_views.LogoutView.as_view(), name='logout'),
#     path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
#     path('get/profile/', Profile.as_view(), name='profile'),
    path('index-market/', IndexMarket.as_view()),
    path('get-all-seller/', AllSeller.as_view()),
    path('get-all-sellerByMarket/<int:market_id>/', AllSellerByMarket.as_view()),
    path('get-all-fisherman/', AllFisherman.as_view()),
    path('add-market/', CreateMarket.as_view()),
    path('delete-market/<int:market_id>/', DeleteMarket.as_view()),
    path('add-entry/', AddEntry.as_view()),
    path('add-user/', AddUser.as_view()),
    path('add-storage-entry/', AddStorageEntry.as_view()),
    path('update-user-name/<int:user_id>/', UpdateUserName.as_view()),
    path('update-user-phone/<int:user_id>/', UpdateUserPhone.as_view()),
    path('update-user-market/<int:user_id>/', UpdateUserMarket.as_view()),
    path('update-entry-quantity/<int:entry_id>/', UpdateEntryQuantity.as_view()),
    path('reset-broken/', reset_broken),
    path('reset-lost/', reset_lost),
    path('deactivate-user-status/<int:user_id>/', deactivate_user_status),
    path('reactivate-user-status/<int:user_id>/', reactivate_user_status),
    path('delete-user/<int:user_id>/', delete_user),
    path('delete-entry/<int:entry_id>/', delete_entry),
    path('delete-storage_entry/<int:storage_entry_id>/', delete_storage_entry),
    path('get-faq/', AllFAQs.as_view()),
    path('get-storage_balance/', get_storage_balance),
    path('get-number_manufactured/', get_number_manufactured),
    path('get-entry_type/', GetEntryType.as_view()),
    path('get-entry-type/<int:entry_id>/', GetEntryTypeObject.as_view()),
    path('get-delete-user/', AllDeletedUsers.as_view()),
    path('get-lost/', get_calculate_lost),
    path('get-storage-entries/', AllStorageEntries.as_view()),
    path('get-broken/', get_broken),
]

