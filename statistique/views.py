import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from client.models import Article, Facture
from depenses.models import Categorie, Depense

# class StatistiquesVentesView(TemplateView):
#     template_name = 'statistique/statistiques_ventes.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         # Ventes Totales par Article
#         ventes_par_article = Article.objects.values('intitule').annotate(
#             total_quantite=Sum('quantite'),
#             total_revenu=Sum('total')
#         )

#         # Tendances de Ventes Mensuelles
#         ventes_par_mois = Facture.objects.annotate(
#             month=TruncMonth('date_creation_facture')
#         ).values('month').annotate(
#             total_quantite=Sum('article__quantite'),
#             total_revenu=Sum('article__total')
#         ).order_by('month')

#         # Articles les Plus Vendus
#         top_articles = Article.objects.values('intitule').annotate(
#             total_quantite=Sum('quantite')
#         ).order_by('-total_quantite')[:5]

#         # Répartition des Ventes
#         distribution_ventes = Article.objects.values('intitule').annotate(
#             total_quantite=Sum('quantite')
#         ).order_by('total_quantite')

#         # Générer les graphiques
#         context['graphique_ventes_par_article'] = self.generate_graph(
#             ventes_par_article, 'Articles', 'Total des ventes', 'Total des ventes par article', 'intitule', 'total_quantite')
#         context['graphique_ventes_par_mois'] = self.generate_graph(
#             ventes_par_mois, 'Mois', 'Total des ventes', 'Total des ventes par mois', 'month', 'total_quantite')
#         context['graphique_top_articles'] = self.generate_graph(
#             top_articles, 'Articles', 'Total des ventes', 'Top 5 des ventes par article', 'intitule', 'total_quantite')
#         context['graphique_distribution_ventes'] = self.generate_graph(
#             distribution_ventes, 'Articles', 'Total des ventes', 'Distribution des ventes par article', 'intitule', 'total_quantite')

#         return context

#     def generate_graph(self, data, xlabel, ylabel, title, label_field, value_field):
#         labels = [item[label_field] for item in data]
#         values = [item[value_field] for item in data]

#         plt.figure(figsize=(10, 6))
#         plt.bar(labels, values)
#         plt.xlabel(xlabel)
#         plt.ylabel(ylabel)
#         plt.title(title)
#         plt.xticks(rotation=45, ha='right')

#         buffer = BytesIO()
#         plt.savefig(buffer, format='png')
#         buffer.seek(0)
#         image_png = buffer.getvalue()
#         buffer.close()
#         plt.close()

#         graphique = base64.b64encode(image_png).decode()
#         return graphique


# class StatistiquesDepensesView(TemplateView):
#     template_name = 'statistique/statistiques_depenses.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         # Dépenses Totales par Catégorie
#         depenses_par_categorie = Categorie.objects.values('intitule').annotate(
#             total_depenses=Sum('depense__montant')
#         )

#         # Tendances de Dépenses Mensuelles
#         depenses_par_mois = Depense.objects.annotate(
#             month=TruncMonth('date_depense')
#         ).values('month').annotate(
#             total_depenses=Sum('montant')
#         ).order_by('month')

#         # Catégories les Plus Dépensées
#         top_categories = Categorie.objects.values('intitule').annotate(
#             total_depenses=Sum('depense__montant')
#         ).order_by('-total_depenses')[:5]

#         # Répartition des Dépenses
#         distribution_depenses = Categorie.objects.values('intitule').annotate(
#             total_depenses=Sum('depense__montant')
#         ).order_by('total_depenses')

#         # Générer les graphiques
#         context['graphique_depenses_par_categorie'] = self.generate_graph(
#             depenses_par_categorie, 'Catégories', 'Total des dépenses', 'Total des dépenses par catégorie', 'intitule', 'total_depenses')
#         context['graphique_depenses_par_mois'] = self.generate_graph(
#             depenses_par_mois, 'Mois', 'Total des dépenses', 'Total des dépenses par mois', 'month', 'total_depenses')
#         context['graphique_top_categories'] = self.generate_graph(
#             top_categories, 'Catégories', 'Total des dépenses', 'Top 5 des dépenses par catégorie', 'intitule', 'total_depenses')
#         context['graphique_distribution_depenses'] = self.generate_graph(
#             distribution_depenses, 'Catégories', 'Total des dépenses', 'Distribution des dépenses par catégorie', 'intitule', 'total_depenses')

#         return context

#     def generate_graph(self, data, xlabel, ylabel, title, label_field, value_field):
#         labels = [item[label_field] for item in data]
#         values = [item[value_field] for item in data]

#         plt.figure(figsize=(10, 6))
#         plt.bar(labels, values)
#         plt.xlabel(xlabel)
#         plt.ylabel(ylabel)
#         plt.title(title)
#         plt.xticks(rotation=45, ha='right')

#         buffer = BytesIO()
#         plt.savefig(buffer, format='png')
#         buffer.seek(0)
#         image_png = buffer.getvalue()
#         buffer.close()
#         plt.close()

#         graphique = base64.b64encode(image_png).decode()
#         return graphique



class StatistiquesVentesView(TemplateView):
    template_name = 'statistique/statistiques_ventes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Ventes Totales par Article
        ventes_par_article = Article.objects.values('intitule').annotate(
            total_quantite=Sum('quantite'),
            total_revenu=Sum('total')
        )

        # Tendances de Ventes Mensuelles
        ventes_par_mois = Facture.objects.annotate(
            month=TruncMonth('date_creation_facture')
        ).values('month').annotate(
            total_quantite=Sum('article__quantite'),
            total_revenu=Sum('article__total')
        ).order_by('month')

        # Articles les Plus Vendus
        top_articles = Article.objects.values('intitule').annotate(
            total_quantite=Sum('quantite')
        ).order_by('-total_quantite')[:5]

        # Répartition des Ventes
        distribution_ventes = Article.objects.values('intitule').annotate(
            total_quantite=Sum('quantite')
        ).order_by('total_quantite')

        # Générer les graphiques
        context['graphique_ventes_par_article'] = self.generate_graph(
            ventes_par_article, 'Articles', 'Total des ventes', 'Total des ventes par article', 'intitule', 'total_quantite')
        context['graphique_ventes_par_mois'] = self.generate_graph(
            ventes_par_mois, 'Mois', 'Total des ventes', 'Total des ventes par mois', 'month', 'total_quantite')
        context['graphique_top_articles'] = self.generate_graph(
            top_articles, 'Articles', 'Total des ventes', 'Top 5 des ventes par article', 'intitule', 'total_quantite')
        context['graphique_distribution_ventes'] = self.generate_graph(
            distribution_ventes, 'Articles', 'Total des ventes', 'Distribution des ventes par article', 'intitule', 'total_quantite')

        return context

    def generate_graph(self, data, xlabel, ylabel, title, label_field, value_field):
        labels = [item[label_field] for item in data]
        values = [item[value_field] for item in data]

        plt.figure(figsize=(10, 6))
        plt.bar(labels, values)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.xticks(rotation=45, ha='right')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        plt.close()

        graphique = base64.b64encode(image_png).decode()
        return graphique


class StatistiquesDepensesView(TemplateView):
    template_name = 'statistique/statistiques_depenses.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Dépenses Totales par Catégorie
        depenses_par_categorie = Categorie.objects.values('intitule').annotate(
            total_depenses=Sum('depense__montant')
        )

        # Tendances de Dépenses Mensuelles
        depenses_par_mois = Depense.objects.annotate(
            month=TruncMonth('date_depense')
        ).values('month').annotate(
            total_depenses=Sum('montant')
        ).order_by('month')

        # Catégories les Plus Dépensées
        top_categories = Categorie.objects.values('intitule').annotate(
            total_depenses=Sum('depense__montant')
        ).order_by('-total_depenses')[:5]

        # Répartition des Dépenses
        distribution_depenses = Categorie.objects.values('intitule').annotate(
            total_depenses=Sum('depense__montant')
        ).order_by('total_depenses')

        # Générer les graphiques
        context['graphique_depenses_par_categorie'] = self.generate_graph(
            depenses_par_categorie, 'Catégories', 'Total des dépenses', 'Total des dépenses par catégorie', 'intitule', 'total_depenses')
        context['graphique_depenses_par_mois'] = self.generate_graph(
            depenses_par_mois, 'Mois', 'Total des dépenses', 'Total des dépenses par mois', 'month', 'total_depenses')
        context['graphique_top_categories'] = self.generate_graph(
            top_categories, 'Catégories', 'Total des dépenses', 'Top 5 des dépenses par catégorie', 'intitule', 'total_depenses')
        context['graphique_distribution_depenses'] = self.generate_graph(
            distribution_depenses, 'Catégories', 'Total des dépenses', 'Distribution des dépenses par catégorie', 'intitule', 'total_depenses')

        return context

    def generate_graph(self, data, xlabel, ylabel, title, label_field, value_field):
        labels = [item[label_field] for item in data]
        values = [item[value_field] for item in data]

        plt.figure(figsize=(10, 6))
        plt.bar(labels, values)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.xticks(rotation=45, ha='right')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        plt.close()

        graphique = base64.b64encode(image_png).decode()
        return graphique
