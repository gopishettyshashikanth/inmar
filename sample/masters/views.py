from django.shortcuts import render
from masters.models import MetaData,SKUdata
import json
import pandas as pd
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import MetaDataSerializer
import logging

logger = logging.getLogger('myapp')

LOCATIONS_COLUMNS = ('location_code','location','department_code','department','category_code','category','subcategory_code','subcategory')
SKUDATA_COLUMNS = ('sku','name','location','department','category','subCategory')

class LocationList(APIView):
	def get(self, request, location_id):
		try:
			logger.info(f"Request received for location_id: {location_id}")
			query_set = MetaData.objects.filter(location_code=location_id).values(*LOCATIONS_COLUMNS)
			if len(query_set) > 0:
				logger.info(f"Found {len(query_set)} records for location_id: {location_id}")
				return Response({"data":list(query_set)}, status=status.HTTP_200_OK)	
			else:
				logger.warning(f"No data found for location_id: {location_id}")
				return Response(
                    {"error": "Data not Found"},
                    status=status.HTTP_404_NOT_FOUND
                )
		except Exception as e:
			logger.error(f"Error occurred while processing location_id {location_id}: {str(e)}")
			return Response(
                {"error": "Internal server error", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class DepartmentList(APIView):
	def get(self, request, location_id, department_id):
		try:
			logger.info(f"Received request for location_id: {location_id}, department_id: {department_id}")
			query_set = MetaData.objects.filter(location_code=location_id, department_code=department_id).values(*LOCATIONS_COLUMNS)
			if len(query_set) > 0:
				logger.info(f"Found {len(query_set)} records for location_id: {location_id}, department_id: {department_id}")
				return Response({"data":list(query_set)}, status=status.HTTP_200_OK)
			else:
				logger.warning(f"No data found for location_id: {location_id}, department_id: {department_id}")
				return Response(
                    {"error": "Data not Found"},
                    status=status.HTTP_404_NOT_FOUND
                )
		except Exception as e:
			logger.error(f"Error occurred while processing location_id: {location_id}, department_id: {department_id}. Error: {str(e)}")
			return Response(
                {"error": "Internal server error", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CategoryList(APIView):
	def get(self, request, location_id, department_id, category_id):
		try:
			logger.info(f"Received request for location_id: {location_id}, department_id: {department_id}, category_id: {category_id}")
			query_set = MetaData.objects.filter(location_code=location_id, department_code=department_id, category_code=category_id).values(*LOCATIONS_COLUMNS)
			if len(query_set) > 0:
				logger.info(f"Found {len(query_set)} records for location_id: {location_id}, department_id: {department_id}, category_id: {category_id}")
				return Response({"data":list(query_set)}, status=status.HTTP_200_OK)
			else:
				logger.warning(f"No data found for location_id: {location_id}, department_id: {department_id}, category_id: {category_id}")
				return Response(
                    {"error": "Data not Found"},
                    status=status.HTTP_404_NOT_FOUND
                )
		except Exception as e:
			logger.error(f"Error occurred while processing location_id: {location_id}, department_id: {department_id}, category_id: {category_id}. Error: {str(e)}")
			return Response(
                {"error": "Internal server error", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class SubCategoryList(APIView):
	def get(self, request, location_id, department_id, category_id, subcategory_id):
		try:
			logger.info(f"Received request for location_id: {location_id}, department_id: {department_id}, category_id: {category_id}, subcategory_id: {subcategory_id}")
			query_set = MetaData.objects.filter(location_code=location_id, department_code=department_id, category_code=category_id, subcategory_code=subcategory_id).values(*LOCATIONS_COLUMNS)
			if len(query_set) > 0:
				logger.info(f"Found {len(query_set)} records for location_id: {location_id}, department_id: {department_id}, category_id: {category_id}, subcategory_id: {subcategory_id}")
				return Response({"data":list(query_set)}, status=status.HTTP_200_OK)	
			else:
				logger.warning(f"No data found for location_id: {location_id}, department_id: {department_id}, category_id: {category_id}, subcategory_id: {subcategory_id}")
				return Response(
                    {"error": "Data not Found"},
                    status=status.HTTP_404_NOT_FOUND
                )
		except Exception as e:
			logger.error(f"Error occurred while processing location_id: {location_id}, department_id: {department_id}, category_id: {category_id}, subcategory_id: {subcategory_id}. Error: {str(e)}")
			return Response(
                {"error": "Internal server error", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

	def put(self, request, subcategory_id):
		try:
			logger.info(f"Received PUT request to update MetaData with subcategory_id: {subcategory_id}")
			instance = MetaData.objects.get(subcategory_code=subcategory_id)
			logger.info(f"MetaData instance found for subcategory_id: {subcategory_id}")
		except MetaData.DoesNotExist:
			logger.warning(f"MetaData not found for subcategory_id: {subcategory_id}")
			return Response(
                {"error": "MetaData not found"},
                status=status.HTTP_404_NOT_FOUND
            )
		serializer = MetaDataSerializer(instance, data=request.data, partial=False)
		if serializer.is_valid():
			logger.info(f"MetaData instance validated successfully. Saving updated data for subcategory_id: {subcategory_id}")
			# Save the updated instance
			serializer.save()
			return Response({"data": serializer.data}, status=status.HTTP_200_OK)
		logger.error(f"Validation failed for subcategory_id: {subcategory_id}. Errors: {serializer.errors}")
		return Response(
			{
			"error": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
            )       


	def delete(self, request, location_id, department_id, category_id, subcategory_id):
		try:
			logger.info(f"Received DELETE request to delete MetaData for location_id: {location_id}, "
                    f"department_id: {department_id}, category_id: {category_id}, subcategory_id: {subcategory_id}")
			query_set = MetaData.objects.filter(location_code=location_id, department_code=department_id, category_code=category_id, subcategory_code=subcategory_id)
			if len(query_set) > 0:
				obj = query_set.delete()
				logger.info("Record is deleted succefully")
				return Response({"data":"Record is deleted succefully"}, status=status.HTTP_200_OK)
			else:
				logger.warning(f"No records found to delete")
				return Response(
                    {"error": "Data not Found"},
                    status=status.HTTP_404_NOT_FOUND
                )	
		except Exception as e:
			logger.error(f"Error occurred while deleting MetaData for location_id: {location_id}, "
                     f"department_id: {department_id}, category_id: {category_id}, subcategory_id: {subcategory_id}. "
                     f"Error: {str(e)}")
			return Response(
                {"error": "Internal server error", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class InsertMetaData(APIView):
	def post(self, request):
		try:
			df = pd.read_csv("masters/locations.csv")
			meta_data = {}
			for each in df.index:
				meta_data['location_code'] = df["Location_Code"][each]
				meta_data['location'] = df["Location"][each]
				meta_data['department_code'] = df["Department_Code"][each]
				meta_data['department'] = df["Department"][each]

				meta_data['category_code'] = df["Category_Code"][each]
				meta_data['category'] = df["Category"][each]
				meta_data['subcategory_code'] = df["SubCategory_Code"][each]
				meta_data['subcategory'] = df["SubCategory"][each]

				#MetaData.objects.create(**meta_data)
				query_set = MetaData.objects.filter(**meta_data)
				if len(query_set) == 0 :
					query_set = MetaData.objects.create(**meta_data)
				else:
					print("Record is already exist")	
			return Response({"data":"Meta Data Records are inserted succefully"}, status=status.HTTP_200_OK)
		except Exception as e:
			return Response(
                {"error": "Internal server error", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class InsertSKUData(APIView):
	def post(self, request):
		try:
			df = pd.read_csv("masters/sku_data.csv")
			sku_data = {}
			for each in df.index:
				sku_data['sku'] = df["SKU"][each]
				sku_data['name'] = df["NAME"][each]
				sku_data['location'] = df["LOCATION"][each]
				sku_data['department'] = df["DEPARTMENT"][each]

				sku_data['category'] = df["CATEGORY"][each]
				sku_data['subCategory'] = df["SUBCATEGORY"][each]

				#SKUdata.objects.create(**sku_data)
				query_set = SKUdata.objects.filter(**sku_data)
				if len(query_set) == 0 :
					query_set = SKUdata.objects.create(**sku_data)

			return Response({"data":"SKU Data Records are inserted succefully"}, status=status.HTTP_200_OK)
		except Exception as e:
			return Response(
                {"error": "Internal server error", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )          	

class AllLocationList(APIView):
	def get(self, request):
		logger.info("Received GET request")
		query_set = MetaData.objects.all().values(*LOCATIONS_COLUMNS)
		return Response({"data":list(query_set)}, status=status.HTTP_200_OK)
	def delete(self, request):
		logger.info("Received DELETE request")
		query_set = MetaData.objects.all().delete()
		return Response({"data":"Records are deleted succefully"}, status=status.HTTP_200_OK)

class CreateMetaDataList(APIView):
	def post(self, request): 
		try:
			logger.info(f"Received POST request with data: {request.data}")
			data = {
				"location_code" : request.data['location_code'],
				"location" : request.data['location'],
				"department_code" : request.data['department_code'],
				"department" : request.data['department'],
				"category_code" : request.data['category_code'],
				"category" : request.data['category'],
				"subcategory_code" : request.data['subCategory_code'],
				"subcategory" : request.data['subCategory'],
			}
			query_set = MetaData.objects.filter(**data)
			if len(query_set) > 0 :
				logger.warning(f"Record already exists with criteria: {data}")
				return Response({"data":"Record already exist"}, status=status.HTTP_200_OK)
			else:
				logger.info(f"No existing record found. Creating a new record with data: {data}")
				query_set = MetaData.objects.create(**data)
				logger.info(f"Record successfully created with data: {data}")
				return Response({"data":"Record is created succefully"}, status=status.HTTP_200_OK)
		except Exception as e:
			logger.error(f"Error occurred while processing POST request. Error: {str(e)}")
			return Response(
                {"error": "Internal server error", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class SKUDataList(APIView):
	def delete(self, request):
		logger.info("Received DELETE request")
		query_set = SKUdata.objects.all().delete()
		return Response({"data":"Records are deleted succefully"}, status=status.HTTP_200_OK)
	
	def post(self, request):
		try:
			logger.info(f"Received POST request with data: {request.data}")
			data = {
				"location" : request.data['location'],
				"department" : request.data['department'],
				"category" : request.data['category'],
				"subCategory" : request.data['subCategory'],
			}
			query_set = SKUdata.objects.filter(**data).values(*SKUDATA_COLUMNS)
			if len(query_set) > 0:
				logger.info(f"Found {len(query_set)} matching records for the given criteria.")
				return Response({"data":list(query_set)}, status=status.HTTP_200_OK)
			else:
				logger.warning(f"No matching records found for the criteria: {data}")
				return Response({"error": "No matching records found"}, status=status.HTTP_404_NOT_FOUND)	
		except Exception as e:
			logger.error(f"Error occurred while processing POST request. Error: {str(e)}")
			return Response(
                {"error": "Internal server error", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


