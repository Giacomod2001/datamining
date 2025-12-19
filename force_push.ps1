# Script per forzare il push della versione locale
# Questo script risolve i conflitti dando priorità alla versione locale

Write-Host "=== Risoluzione conflitti di merge ===" -ForegroundColor Cyan
Write-Host "Priorità: versione LOCALE" -ForegroundColor Yellow
Write-Host ""

# Verifica se esiste .git
if (-Not (Test-Path ".git")) {
    Write-Host "ERRORE: Questa directory non è un repository Git!" -ForegroundColor Red
    exit 1
}

Write-Host "Istruzioni per GitHub Desktop:" -ForegroundColor Green
Write-Host "1. In GitHub Desktop, vai su Branch > Merge into current branch" -ForegroundColor White
Write-Host "2. Se ci sono conflitti, clicca su 'Open in Visual Studio Code'" -ForegroundColor White
Write-Host "3. Per ogni file in conflitto, clicca 'Accept Current Change' (versione locale)" -ForegroundColor White
Write-Host "4. Salva i file e torna a GitHub Desktop" -ForegroundColor White
Write-Host "5. Clicca 'Continue merge' e poi 'Push origin'" -ForegroundColor White
Write-Host ""
Write-Host "ALTERNATIVA - Forzare push della versione locale:" -ForegroundColor Yellow
Write-Host "Se vuoi sovrascrivere completamente il repository remoto:" -ForegroundColor Yellow
Write-Host "1. In GitHub Desktop, vai su Repository > Repository Settings" -ForegroundColor White
Write-Host "2. Oppure usa questo comando in un terminale con Git installato:" -ForegroundColor White
Write-Host "   git push --force origin main" -ForegroundColor Cyan
Write-Host ""
Write-Host "ATTENZIONE: Force push sovrascriverà TUTTE le modifiche remote!" -ForegroundColor Red
