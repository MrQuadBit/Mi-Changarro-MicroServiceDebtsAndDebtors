<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

	<xsl:output method="html"/>

	<xsl:template match="/">
		<html>
			<body>
				<h1>Deudas y Deudores</h1>
				<table border="1">
					<tr bgcolor="red">
						<th>Tipo</th>
						<th>Nombre</th>
						<th>Cantidad</th>
					</tr>
					<xsl:apply-templates/>
				</table>
			</body>
		</html>
	</xsl:template>

	<xsl:template match="debts_and_debtors">
		<xsl:for-each select="person">
			<tr>
				<xsl:choose>
					<xsl:when test="@type > 0">
						<td>Deuda</td>
					</xsl:when>
					<xsl:otherwise>
						<td>Deudor</td>
					</xsl:otherwise>
				</xsl:choose>
				<td><xsl:value-of select="name"/></td>
				<td><xsl:value-of select="quantity"/></td>
				
			</tr>
		</xsl:for-each>
	</xsl:template>

</xsl:stylesheet>

