from django.contrib import admin
from django.db.models import Q


class ModelAdminNotCaseSensitiveSearch(admin.ModelAdmin):
    def get_search_results(self, request, queryset, search_term):
        """Override get_search_results to enable case-insensitive search."""
        queryset, use_distinct = super().get_search_results(
            request, queryset, search_term
        )
        if search_term:
            query = None
            for term in self.search_fields:
                # Create a case-insensitive query for each search field
                q = Q(**{f"{term}__icontains": search_term})
                query = q if query is None else query | q

            queryset = queryset.filter(query)

        return queryset, use_distinct
