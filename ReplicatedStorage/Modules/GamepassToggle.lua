local Players = game:GetService("Players")
local MarketplaceService = game:GetService("MarketplaceService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local GamepassService = require(ReplicatedStorage.Modules.GamepassService)
local GamepassConfig = require(ReplicatedStorage.Config.GamepassConfig)

local GamepassToggle = {}

-- Setup a part as a toggle for a specific gamepass.
-- options = {
--     part = <Model or BasePart>,
--     passName = "AUTO_COLLECT",
--     attribute = "AutoCollectActive",
--     cooldown = number -- optional (default 1.5)
-- }
function GamepassToggle.Setup(options)
    assert(options and options.part and options.passName and options.attribute, "GamepassToggle.Setup missing required options")
    local part = options.part
    local passName = options.passName
    local attribute = options.attribute
    local cooldown = options.cooldown or 1.5
    local promptCooldown = options.promptCooldown or 5

    local gamepassId = GamepassConfig.GetId(passName)
    if not gamepassId then
        warn("GamepassToggle: Unknown gamepass", passName)
        return
    end

    local prompted = {}
    local toggles = {}
    local owners = {}
    local cooldowns = {}

    local function updateVisual(player, owns, isActive)
        if not player or not player:IsDescendantOf(Players) then return end
        local model = part
        local topPart = model:FindFirstChild("Top")
        local bottomPart = model:FindFirstChild("Bottom")
        if not topPart or not bottomPart then return end
        if not owns then
            topPart.BrickColor = BrickColor.new("New Yeller")
            bottomPart.BrickColor = BrickColor.new("Deep orange")
        elseif isActive then
            topPart.BrickColor = BrickColor.new("Bright green")
            bottomPart.BrickColor = BrickColor.new("Forest green")
        else
            topPart.BrickColor = BrickColor.new("Bright red")
            bottomPart.BrickColor = BrickColor.new("Medium red")
        end
    end

    local function hasPass(player)
        if owners[player.UserId] ~= nil then
            return owners[player.UserId]
        end
        local owns = GamepassService.PlayerOwns(player, passName)
        owners[player.UserId] = owns
        return owns
    end

    part.Touched:Connect(function(hit)
        local character = hit:FindFirstAncestorOfClass("Model")
        local player = character and Players:GetPlayerFromCharacter(character)
        if not player then return end

        if cooldowns[player.UserId] and tick() - cooldowns[player.UserId] < cooldown then
            return
        end
        cooldowns[player.UserId] = tick()

        local owns = hasPass(player)
        if not owns then
            if not prompted[player.UserId] then
                prompted[player.UserId] = true
                MarketplaceService:PromptGamePassPurchase(player, gamepassId)
                task.delay(promptCooldown, function()
                    prompted[player.UserId] = nil
                end)
            end
            updateVisual(player, false, false)
            return
        end

        toggles[player.UserId] = not toggles[player.UserId]
        local isActive = toggles[player.UserId]
        player:SetAttribute(attribute, isActive)
        updateVisual(player, true, isActive)
    end)

    MarketplaceService.PromptGamePassPurchaseFinished:Connect(function(player, id, purchased)
        if id == gamepassId and purchased then
            owners[player.UserId] = true
            toggles[player.UserId] = true
            player:SetAttribute(attribute, true)
            updateVisual(player, true, true)
        end
    end)

    Players.PlayerAdded:Connect(function(player)
        task.defer(function()
            local owns = hasPass(player)
            toggles[player.UserId] = owns and true or false
            player:SetAttribute(attribute, toggles[player.UserId])
            updateVisual(player, owns, toggles[player.UserId])
        end)
    end)
end

return GamepassToggle
