This is a Vendor Management System developed using Django and Django REST Framework. The system allows you to manage vendor profiles, track purchase orders, and calculate performance metrics for vendors.
Features
Vendor Profile Management:

Create, retrieve, update, and delete vendor profiles.
Purchase Order Tracking:

Create, retrieve, update, and delete purchase orders.
Filter purchase orders by vendor.
Vendor Performance Evaluation:

Calculate and retrieve performance metrics for vendors.
Performance metrics include on-time delivery rate, quality rating average, average response time, and fulfillment rate.



Models
Vendor Model:

Fields: name, contact_details, address, vendor_code, on_time_delivery_rate, quality_rating_avg, average_response_time, fulfillment_rate.
Purchase Order Model:

Fields: po_number, vendor, order_date, delivery_date, items, quantity, status, quality_rating, issue_date, acknowledgment_date.
Historical Performance Model:

Fields: vendor, date, on_time_delivery_rate, quality_rating_avg, average_response_time, fulfillment_rate.


Certainly! Below is a basic README template for your Vendor Management System with Performance Metrics developed using Django and Django REST Framework. Remember to adapt it according to your project structure, technologies, and any additional details specific to your implementation.

Vendor Management System with Performance Metrics
Overview
This is a Vendor Management System developed using Django and Django REST Framework. The system allows you to manage vendor profiles, track purchase orders, and calculate performance metrics for vendors.

Table of Contents
Features
Models
API Endpoints
Backend Logic
Additional Technical Considerations
Technical Requirements
Deliverables
Submission Guidelines
Features
Vendor Profile Management:

Create, retrieve, update, and delete vendor profiles.
Purchase Order Tracking:

Create, retrieve, update, and delete purchase orders.
Filter purchase orders by vendor.
Vendor Performance Evaluation:

Calculate and retrieve performance metrics for vendors.
Performance metrics include on-time delivery rate, quality rating average, average response time, and fulfillment rate.
Models
Vendor Model:

Fields: name, contact_details, address, vendor_code, on_time_delivery_rate, quality_rating_avg, average_response_time, fulfillment_rate.
Purchase Order Model:

Fields: po_number, vendor, order_date, delivery_date, items, quantity, status, quality_rating, issue_date, acknowledgment_date.
Historical Performance Model:

Fields: vendor, date, on_time_delivery_rate, quality_rating_avg, average_response_time, fulfillment_rate.
API Endpoints
Vendor Profile Management:

POST /api/vendors/
GET /api/vendors/
GET /api/vendors/{vendor_id}/
PUT /api/vendors/{vendor_id}/
DELETE /api/vendors/{vendor_id}/
Purchase Order Tracking:

POST /api/purchase_orders/
GET /api/purchase_orders/
GET /api/purchase_orders/{po_id}/
PUT /api/purchase_orders/{po_id}/
DELETE /api/purchase_orders/{po_id}/
Vendor Performance Evaluation:

GET /api/vendors/{vendor_id}/performance/


Logic to get following
On-Time Delivery Rate:

Calculated each time a purchase order status changes to 'completed'.
Logic: Count the number of completed purchase orders delivered on or before delivery_date and divide by the total number of completed purchase orders for that vendor.
Quality Rating Average:

Updated upon the completion of each purchase order where a quality_rating is provided.
Logic: Calculate the average of all quality_rating values for completed purchase orders of the vendor.
Average Response Time:

Calculated each time a purchase order is acknowledged by the vendor.
Logic: Compute the time difference between issue_date and acknowledgment_date for each purchase order, then find the average of these times for all purchase orders of the vendor.
Fulfillment Rate:

Calculated upon any change in purchase order status.
Logic: Divide the number of successfully fulfilled purchase orders (status 'completed' without issues) by the total number of purchase orders issued to the vendor.

